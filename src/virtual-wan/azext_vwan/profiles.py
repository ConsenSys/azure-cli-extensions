# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.profiles import CustomResourceType

CUSTOM_VWAN = CustomResourceType('azext_vwan.vendored_sdks.v2021_08_01', 'NetworkManagementClient')
