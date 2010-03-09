"""
shop.settings - these are the settings and their default values used internally 
throughout the shop. each should set in your project's settings module using the 
prefix SHOP_setting_name eg: SHOP_PRODUCT_OPTIONS
"""

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

# number of minutes of inactivity for carts until they're abandoned
CART_EXPIRY_MINUTES = getattr(settings, "SHOP_CART_EXPIRY_MINUTES", 30) 

# sequence of available credit card types for payment
CARD_TYPES = getattr(settings, "SHOP_CARD_TYPES", 
    ("Mastercard", "Visa", "Diners", "Amex")
)

# controls the display formatting of monetary values accord to the locale 
# module in the python standard library
CURRENCY_LOCALE = getattr(settings, "SHOP_CURRENCY_LOCALE", "")

# sequence of pairs for order statuses
ORDER_STATUSES = getattr(settings, "SHOP_ORDER_STATUSES", (
    (1, _("Unprocessed")),
    (2, _("Processed")),
))

# default order status for new orders
ORDER_STATUS_DEFAULT = getattr(settings, "SHOP_ORDER_STATUS_DEFAULT", 1)

# sequence of name/sequence pairs defining the selectable options for products
PRODUCT_OPTIONS = getattr(settings, "SHOP_PRODUCT_OPTIONS", (
    ("size", ("Extra Small","Small","Regular","Large","Extra Large")),
    ("colour", ("Red","Orange","Yellow","Green","Blue","Indigo","Violet")),
))

# email address that order receipts should be emailed from
ORDER_FROM_EMAIL = getattr(settings, "SHOP_ORDER_FROM_EMAIL", None)

# bool to enable automatic redirecting to and from https for checkout
SSL_ENABLED = getattr(settings, "SHOP_SSL_ENABLED", not settings.DEBUG)

# host name matching the ssl cert that the site should always be accessed via
FORCE_HOST = getattr(settings, "SHOP_FORCE_HOST", None)

# number of search results to display per page
SEARCH_RESULTS_PER_PAGE = getattr(settings, "SHOP_SEARCH_RESULTS_PER_PAGE", 10)

ADMIN_REORDER = tuple(getattr(settings, "ADMIN_REORDER", ()))
if "shop" not in dict(ADMIN_REORDER):
    ADMIN_REORDER += (("shop", ("Category", "Product", "Sale", "DiscountCode",
        "Order")),)

