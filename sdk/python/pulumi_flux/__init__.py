# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from . import _utilities
import typing
# Export this package's modules as members:
from .data_install import *
from .data_sync import *
from .provider import *
_utilities.register(
    resource_modules="""
[]
""",
    resource_packages="""
[
 {
  "pkg": "flux",
  "token": "pulumi:providers:flux",
  "fqn": "pulumi_flux",
  "class": "Provider"
 }
]
"""
)
