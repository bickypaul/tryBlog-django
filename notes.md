## Paginator

from django.core.paginator import Paginator

>>>posts = ['1','2','3','4','5']    #list of short strings
>>>p = Paginator(post, 2)           #creatin a paginator object
>>>p.num_pages                      #number of pages
3
>>>for page in p.page_range:        #page_range is an attribute not a method.
...    print(page)
...
1                                   #loops over those pages
2
3
>>> p1 = p.page(1)                  # to look at a specific page
>>>
>>> p1
<Page 1 of 3>
>>> p1.number                       # to get a specific page number
1
>>> p1.object_list                  # to look content of the page in that page  
['1','2']
>>>p1.has_previous()                # this is a method
False
>>>p1.has_next()                    # to check has next page
True
>>>page.next_page_number()          #to check the next page number
2
>>>

## Variables passed to the template by the ListView

1. is_paginated
2. page_obj
