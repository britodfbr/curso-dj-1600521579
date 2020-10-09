# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@britodfbr'

from .models import Link


def ctx_social(request):
    ctx_social_dict = {link.key: link.url for link in Link.objects.all()}
    return ctx_social_dict
