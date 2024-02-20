from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin  # For customizing User display
from .models import UserProfile, Book, Order, BookStoreUser
from django.contrib.auth.models import User

# Customize the User admin view
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'User Profiles'

class CustomUserAdmin(BookStoreUser):
    inlines = (UserProfileInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    list_select_related = ('userprofile',)
    search_fields = ('username', 'email', 'first_name', 'last_name')

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price')
    list_filter = ('author', 'price')
    search_fields = ('title', 'author')


class BookInline(admin.TabularInline):
    model = Book
    can_delete = False
    verbose_name_plural = 'Book Profiles'

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'quantity', 'order_date', 'valid_till')
    list_filter = ('user', 'book', 'order_date', 'valid_till')
    search_fields = ('user', 'book', 'order_date', 'valid_till')


class OrderInline(admin.TabularInline):
    model = Order
    can_delete = False
    verbose_name_plural = 'Order History'

# Register the User model with the CustomUserAdmin
admin.site.register(Book, BookAdmin)
admin.site.register(Order, OrderAdmin)

admin.site.register(BookStoreUser, CustomUserAdmin)
