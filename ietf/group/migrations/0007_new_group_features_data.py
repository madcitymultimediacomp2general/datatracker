# Copyright The IETF Trust 2019, All Rights Reserved
# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-09 09:02
from __future__ import unicode_literals


from django.db import migrations

import debug                            # pyflakes:ignore

group_type_features = {
    u'ag': {
        'custom_group_roles': True,
        'has_session_materials': True,
        'acts_like_wg': True,
        'create_wiki': True,
        'is_schedulable': True,
        'req_subm_approval': True,
        'show_on_agenda': True,
        'matman_roles': ['ad', 'chair', 'delegate', 'secr'],
        'role_order': ['chair', 'secr'],
    },
    u'area': {
        'custom_group_roles': True,
        'has_session_materials': False,
        'acts_like_wg': False,
        'create_wiki': True,
        'is_schedulable': False,
        'req_subm_approval': True,
        'show_on_agenda': False,
        'matman_roles': ['ad', 'chair', 'delegate', 'secr'],
        'role_order': ['chair', 'secr'],
        },
    u'dir': {
        'custom_group_roles': True,
        'has_session_materials': False,
        'acts_like_wg': False,
        'create_wiki': True,
        'is_schedulable': False,
        'req_subm_approval': True,
        'show_on_agenda': False,
        'matman_roles': ['ad', 'chair', 'delegate', 'secr'],
        'role_order': ['chair', 'secr'],
        },
    u'review': {
        'custom_group_roles': True,
        'has_session_materials': False,
        'acts_like_wg': False,
        'create_wiki': True,
        'is_schedulable': False,
        'req_subm_approval': True,
        'show_on_agenda': False,
        'matman_roles': ['ad', 'secr'],
        'role_order': ['chair', 'secr'],
        },
    u'iab': {
        'custom_group_roles': True,
        'has_session_materials': False,
        'acts_like_wg': False,
        'create_wiki': False,
        'is_schedulable': False,
        'req_subm_approval': True,
        'show_on_agenda': True,
        'matman_roles': [],
        'role_order': ['chair', 'secr'],
        },
    u'ietf': {
        'custom_group_roles': True,
        'has_session_materials': True,
        'acts_like_wg': False,
        'create_wiki': False,
        'is_schedulable': False,
        'req_subm_approval': True,
        'show_on_agenda': False,
        'matman_roles': ['chair', 'delegate'],
        'role_order': ['chair', 'secr'],
        },
    u'individ': {
        'custom_group_roles': True,
        'has_session_materials': False,
        'acts_like_wg': False,
        'create_wiki': False,
        'is_schedulable': False,
        'req_subm_approval': False,
        'show_on_agenda': False,
        'matman_roles': ['auth'],
        'role_order': ['chair', 'secr'],
        },
    u'irtf': {
        'custom_group_roles': True,
        'has_session_materials': False,
        'acts_like_wg': False,
        'create_wiki': False,
        'is_schedulable': False,
        'req_subm_approval': True,
        'show_on_agenda': False,
        'matman_roles': ['chair', 'delegate', 'secr'],
        'role_order': ['chair', 'secr'],
        },
    u'isoc': {
        'custom_group_roles': True,
        'has_session_materials': False,
        'acts_like_wg': False,
        'create_wiki': False,
        'is_schedulable': False,
        'req_subm_approval': True,
        'show_on_agenda': False,
        'matman_roles': ['chair', 'secr'],
        'role_order': ['chair', 'secr'],
        },
    u'nomcom': {
        'custom_group_roles': True,
        'has_session_materials': False,
        'acts_like_wg': False,
        'create_wiki': True,
        'is_schedulable': False,
        'req_subm_approval': True,
        'show_on_agenda': False,
        'matman_roles': ['chair'],
        'role_order': ['chair', 'member', 'advisor'],
        },
    u'program': {
        'custom_group_roles': True,
        'has_session_materials': False,
        'acts_like_wg': False,
        'create_wiki': False,
        'is_schedulable': False,
        'req_subm_approval': False,
        'show_on_agenda': False,
        'matman_roles': ['chair', 'secr'],
        'role_order': ['chair', 'secr'],
        },
    u'rfcedtyp': {
        'custom_group_roles': True,
        'has_session_materials': False,
        'acts_like_wg': False,
        'create_wiki': False,
        'is_schedulable': False,
        'req_subm_approval': True,
        'show_on_agenda': False,
        'matman_roles': ['chair', 'secr'],
        'role_order': ['chair', 'secr'],
        },
    u'rg': {
        'custom_group_roles': False,
        'has_session_materials': True,
        'acts_like_wg': True,
        'create_wiki': True,
        'is_schedulable': True,
        'req_subm_approval': True,
        'show_on_agenda': True,
        'matman_roles': ['chair', 'secr'],
        'role_order': ['chair', 'secr'],
        },
    u'sdo': {
        'custom_group_roles': True,
        'has_session_materials': False,
        'acts_like_wg': False,
        'create_wiki': False,
        'is_schedulable': False,
        'req_subm_approval': True,
        'show_on_agenda': False,
        'matman_roles': ['liaiman', 'matman'],
        'role_order': ['liaiman'],
        },
    u'team': {
        'custom_group_roles': True,
        'has_session_materials': False,
        'acts_like_wg': False,
        'create_wiki': True,
        'is_schedulable': False,
        'req_subm_approval': False,
        'show_on_agenda': False,
        'matman_roles': ['chair', 'matman'],
        'role_order': ['chair', 'member', 'matman'],
        },
    u'wg': {
        'custom_group_roles': False,
        'has_session_materials': True,
        'acts_like_wg': True,
        'create_wiki': True,
        'is_schedulable': True,
        'req_subm_approval': True,
        'show_on_agenda': True,
        'matman_roles': ['ad', 'chair', 'delegate', 'secr'],
        'role_order': ['chair', 'secr', 'delegate'],
        },
}

def forward(apps, schema_editor):
    GroupFeatures = apps.get_model('group', 'GroupFeatures')
    for type in group_type_features:
        features = group_type_features[type]
        gf = GroupFeatures.objects.get(type=type)
        for k,v in features.items():
            setattr(gf, k, v)
        gf.save()
forward.interleavable = True

def reverse(apps, schema_editor):
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('group', '0006_group_features_lists_to_jsonfield')
    ]

    operations = [
        migrations.RunPython(forward, reverse),
    ]
