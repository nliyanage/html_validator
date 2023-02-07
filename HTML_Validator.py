#!/bin/python3


import re


def validate_html(html):
    '''
    This function performs a limited version of html
    validation by checking whether every opening tag
    has a corresponding closing tag!

    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''

    # HINT:
    # use the _extract_tags function below to generate a
    # list of html tags without any extra text;
    # then process these html tags using the balanced
    # parentheses algorithm from the class/book
    # the main difference between your code and
    # the code from class will be that you will have
    # to keep track of not just the 3 types of parentheses,
    # but arbitrary text located between the html tags
    taglist = _extract_tags(html)
    if len(html) == 0:
        return True
    if not taglist:
        return False
    stack = []
    index = 0
    balanced = True
    while index < len(taglist) and balanced:
        tag = taglist[index]
        tagname = tag[1:-1]
        if '/' not in tag:
            stack.append(tagname)
        else:
            if len(stack) == 0:
                balanced = False
            else:
                item = stack.pop()
                if not item == tagname[1:]:
                    balanced = False
        index += 1
    if balanced and not stack:
        return True
    else:
        return False


def _extract_tags(html):
    '''
    This is a helper function for `validate_html`.
    By convention in Python, helper functions that are
    not meant to be used directly by the
    user are prefixed with an underscore.

    This function returns a list of all
    the html tags contained in the input string,
    stripping out all text not contained within angle brackets.

    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    '''
    tags = re.findall(r'<[^>]+>', html)
    return tags
