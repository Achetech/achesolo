# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

class BaseConfig(object):

    # Can be set to 'MasterUser' or 'ServicePrincipal'
    AUTHENTICATION_MODE = 'ServicePrincipal'

    # Workspace Id in which the report is present
    WORKSPACE_ID = '7e414492-f302-4c81-838b-82ad12df01e4'
    
    # Report Id for which Embed token needs to be generated
    REPORT_ID = 'dc35557b-1c30-4ebe-a4e9-cf6b714520b5'
    
    # Id of the Azure tenant in which AAD app and Power BI report is hosted. Required only for ServicePrincipal authentication mode.
    TENANT_ID = '550e8027-4b22-443a-a700-72cada0b8442'
    
    # Client Id (Application Id) of the AAD app
    CLIENT_ID = '1fb56356-ed8f-453d-b7d3-e02114dacfd0'
    
    # Client Secret (App Secret) of the AAD app. Required only for ServicePrincipal authentication mode.
    CLIENT_SECRET = 'Pds8Q~qIB7pF34b0Zb_bDWaj0-_G~70aVpDHFaEQ'
    
    # Scope Base of AAD app. Use the below configuration to use all the permissions provided in the AAD app through Azure portal.
    SCOPE_BASE = ['https://analysis.windows.net/powerbi/api/.default']
    
    # URL used for initiating authorization request
    AUTHORITY_URL = 'https://login.microsoftonline.com/organizations'
    
    # Master user email address. Required only for MasterUser authentication mode.
    POWER_BI_USER = ''
    
    # Master user email password. Required only for MasterUser authentication mode.
    POWER_BI_PASS = ''