from pyrpg.attr import Attr

attr = Attr('HP')
attr._upper = 50
attr._lower = 0
attr.set_value(0)
attr.vary_by_amount(25)
attr.vary_to(-1.1)
print(attr._value)