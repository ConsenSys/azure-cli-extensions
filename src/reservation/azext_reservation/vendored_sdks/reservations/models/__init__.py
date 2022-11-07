# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import AppliedReservationList
from ._models_py3 import AppliedReservations
from ._models_py3 import AvailableScopeProperties
from ._models_py3 import AvailableScopeRequest
from ._models_py3 import AvailableScopeRequestProperties
from ._models_py3 import BillingInformation
from ._models_py3 import CalculateExchangeOperationResultResponse
from ._models_py3 import CalculateExchangeRequest
from ._models_py3 import CalculateExchangeRequestProperties
from ._models_py3 import CalculateExchangeResponseProperties
from ._models_py3 import CalculatePriceResponse
from ._models_py3 import CalculatePriceResponseProperties
from ._models_py3 import CalculatePriceResponsePropertiesBillingCurrencyTotal
from ._models_py3 import CalculatePriceResponsePropertiesPricingCurrencyTotal
from ._models_py3 import CalculateRefundRequest
from ._models_py3 import CalculateRefundRequestProperties
from ._models_py3 import CalculateRefundResponse
from ._models_py3 import Catalog
from ._models_py3 import CatalogMsrp
from ._models_py3 import ChangeDirectoryRequest
from ._models_py3 import ChangeDirectoryResponse
from ._models_py3 import ChangeDirectoryResult
from ._models_py3 import CreateGenericQuotaRequestParameters
from ._models_py3 import CurrentQuotaLimit
from ._models_py3 import CurrentQuotaLimitBase
from ._models_py3 import Error
from ._models_py3 import ErrorDetails
from ._models_py3 import ErrorResponse
from ._models_py3 import ExceptionResponse
from ._models_py3 import ExchangeOperationResultResponse
from ._models_py3 import ExchangePolicyError
from ._models_py3 import ExchangePolicyErrors
from ._models_py3 import ExchangeRequest
from ._models_py3 import ExchangeRequestProperties
from ._models_py3 import ExchangeResponseProperties
from ._models_py3 import ExtendedErrorInfo
from ._models_py3 import ExtendedStatusInfo
from ._models_py3 import MergeRequest
from ._models_py3 import OperationDisplay
from ._models_py3 import OperationList
from ._models_py3 import OperationResponse
from ._models_py3 import OperationResultError
from ._models_py3 import Patch
from ._models_py3 import PatchPropertiesRenewProperties
from ._models_py3 import PaymentDetail
from ._models_py3 import Price
from ._models_py3 import PurchaseRequest
from ._models_py3 import PurchaseRequestPropertiesReservedResourceProperties
from ._models_py3 import QuotaLimits
from ._models_py3 import QuotaLimitsResponse
from ._models_py3 import QuotaProperties
from ._models_py3 import QuotaRequestDetails
from ._models_py3 import QuotaRequestDetailsList
from ._models_py3 import QuotaRequestOneResourceSubmitResponse
from ._models_py3 import QuotaRequestProperties
from ._models_py3 import QuotaRequestSubmitResponse
from ._models_py3 import QuotaRequestSubmitResponse201
from ._models_py3 import RefundBillingInformation
from ._models_py3 import RefundPolicyError
from ._models_py3 import RefundPolicyResult
from ._models_py3 import RefundPolicyResultProperty
from ._models_py3 import RefundRequest
from ._models_py3 import RefundRequestProperties
from ._models_py3 import RefundResponse
from ._models_py3 import RefundResponseProperties
from ._models_py3 import RenewPropertiesResponse
from ._models_py3 import RenewPropertiesResponseBillingCurrencyTotal
from ._models_py3 import RenewPropertiesResponsePricingCurrencyTotal
from ._models_py3 import ReservationList
from ._models_py3 import ReservationMergeProperties
from ._models_py3 import ReservationOrderBillingPlanInformation
from ._models_py3 import ReservationOrderList
from ._models_py3 import ReservationOrderResponse
from ._models_py3 import ReservationResponse
from ._models_py3 import ReservationSplitProperties
from ._models_py3 import ReservationSummary
from ._models_py3 import ReservationToExchange
from ._models_py3 import ReservationToPurchaseCalculateExchange
from ._models_py3 import ReservationToPurchaseExchange
from ._models_py3 import ReservationToReturn
from ._models_py3 import ReservationToReturnForExchange
from ._models_py3 import ReservationUtilizationAggregates
from ._models_py3 import ReservationsListResult
from ._models_py3 import ReservationsProperties
from ._models_py3 import ReservationsPropertiesUtilization
from ._models_py3 import ResourceName
from ._models_py3 import ScopeProperties
from ._models_py3 import ServiceError
from ._models_py3 import ServiceErrorDetail
from ._models_py3 import SkuCapability
from ._models_py3 import SkuName
from ._models_py3 import SkuProperty
from ._models_py3 import SkuRestriction
from ._models_py3 import SplitRequest
from ._models_py3 import SubRequest
from ._models_py3 import SubscriptionScopeProperties
from ._models_py3 import SystemData

from ._azure_reservation_api_enums import AppliedScopeType
from ._azure_reservation_api_enums import CalculateExchangeOperationResultStatus
from ._azure_reservation_api_enums import CreatedByType
from ._azure_reservation_api_enums import DisplayProvisioningState
from ._azure_reservation_api_enums import ErrorResponseCode
from ._azure_reservation_api_enums import ExchangeOperationResultStatus
from ._azure_reservation_api_enums import InstanceFlexibility
from ._azure_reservation_api_enums import Location
from ._azure_reservation_api_enums import OperationStatus
from ._azure_reservation_api_enums import PaymentStatus
from ._azure_reservation_api_enums import ProvisioningState
from ._azure_reservation_api_enums import QuotaRequestState
from ._azure_reservation_api_enums import ReservationBillingPlan
from ._azure_reservation_api_enums import ReservationStatusCode
from ._azure_reservation_api_enums import ReservationTerm
from ._azure_reservation_api_enums import ReservedResourceType
from ._azure_reservation_api_enums import ResourceType
from ._azure_reservation_api_enums import UserFriendlyAppliedScopeType
from ._azure_reservation_api_enums import UserFriendlyRenewState
from ._patch import __all__ as _patch_all
from ._patch import *  # type: ignore # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "AppliedReservationList",
    "AppliedReservations",
    "AvailableScopeProperties",
    "AvailableScopeRequest",
    "AvailableScopeRequestProperties",
    "BillingInformation",
    "CalculateExchangeOperationResultResponse",
    "CalculateExchangeRequest",
    "CalculateExchangeRequestProperties",
    "CalculateExchangeResponseProperties",
    "CalculatePriceResponse",
    "CalculatePriceResponseProperties",
    "CalculatePriceResponsePropertiesBillingCurrencyTotal",
    "CalculatePriceResponsePropertiesPricingCurrencyTotal",
    "CalculateRefundRequest",
    "CalculateRefundRequestProperties",
    "CalculateRefundResponse",
    "Catalog",
    "CatalogMsrp",
    "ChangeDirectoryRequest",
    "ChangeDirectoryResponse",
    "ChangeDirectoryResult",
    "CreateGenericQuotaRequestParameters",
    "CurrentQuotaLimit",
    "CurrentQuotaLimitBase",
    "Error",
    "ErrorDetails",
    "ErrorResponse",
    "ExceptionResponse",
    "ExchangeOperationResultResponse",
    "ExchangePolicyError",
    "ExchangePolicyErrors",
    "ExchangeRequest",
    "ExchangeRequestProperties",
    "ExchangeResponseProperties",
    "ExtendedErrorInfo",
    "ExtendedStatusInfo",
    "MergeRequest",
    "OperationDisplay",
    "OperationList",
    "OperationResponse",
    "OperationResultError",
    "Patch",
    "PatchPropertiesRenewProperties",
    "PaymentDetail",
    "Price",
    "PurchaseRequest",
    "PurchaseRequestPropertiesReservedResourceProperties",
    "QuotaLimits",
    "QuotaLimitsResponse",
    "QuotaProperties",
    "QuotaRequestDetails",
    "QuotaRequestDetailsList",
    "QuotaRequestOneResourceSubmitResponse",
    "QuotaRequestProperties",
    "QuotaRequestSubmitResponse",
    "QuotaRequestSubmitResponse201",
    "RefundBillingInformation",
    "RefundPolicyError",
    "RefundPolicyResult",
    "RefundPolicyResultProperty",
    "RefundRequest",
    "RefundRequestProperties",
    "RefundResponse",
    "RefundResponseProperties",
    "RenewPropertiesResponse",
    "RenewPropertiesResponseBillingCurrencyTotal",
    "RenewPropertiesResponsePricingCurrencyTotal",
    "ReservationList",
    "ReservationMergeProperties",
    "ReservationOrderBillingPlanInformation",
    "ReservationOrderList",
    "ReservationOrderResponse",
    "ReservationResponse",
    "ReservationSplitProperties",
    "ReservationSummary",
    "ReservationToExchange",
    "ReservationToPurchaseCalculateExchange",
    "ReservationToPurchaseExchange",
    "ReservationToReturn",
    "ReservationToReturnForExchange",
    "ReservationUtilizationAggregates",
    "ReservationsListResult",
    "ReservationsProperties",
    "ReservationsPropertiesUtilization",
    "ResourceName",
    "ScopeProperties",
    "ServiceError",
    "ServiceErrorDetail",
    "SkuCapability",
    "SkuName",
    "SkuProperty",
    "SkuRestriction",
    "SplitRequest",
    "SubRequest",
    "SubscriptionScopeProperties",
    "SystemData",
    "AppliedScopeType",
    "CalculateExchangeOperationResultStatus",
    "CreatedByType",
    "DisplayProvisioningState",
    "ErrorResponseCode",
    "ExchangeOperationResultStatus",
    "InstanceFlexibility",
    "Location",
    "OperationStatus",
    "PaymentStatus",
    "ProvisioningState",
    "QuotaRequestState",
    "ReservationBillingPlan",
    "ReservationStatusCode",
    "ReservationTerm",
    "ReservedResourceType",
    "ResourceType",
    "UserFriendlyAppliedScopeType",
    "UserFriendlyRenewState",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
