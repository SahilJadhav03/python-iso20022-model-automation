from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlTime

from python_iso20022.auth.enums import (
    BenchmarkCurveName2Code,
    CommunicationMethod4Code,
    PaymentScheduleType2Code,
    RateBasis1Code,
)
from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import (
    AddressType2Code,
    CreditDebit3Code,
    DepositType1Code,
    ExchangeRateType1Code,
    NamePrefix2Code,
    PreferredContactMethod2Code,
    QueryType3Code,
    TaxExemptReason1Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04"


@dataclass
class AccountSchemeName1ChoiceAuth02200104(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ActiveCurrencyAndAmountAuth02200104(ISO20022MessageElement):
    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 5,
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )


@dataclass
class BinaryFile1Auth02200104(ISO20022MessageElement):
    mimetp: Optional[str] = field(
        default=None,
        metadata={
            "name": "MIMETp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ncodg_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "NcodgTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    char_set: Optional[str] = field(
        default=None,
        metadata={
            "name": "CharSet",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    incl_binry_objct: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "InclBinryObjct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 102400,
            "format": "base64",
        },
    )


@dataclass
class CashAccountType2ChoiceAuth02200104(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ClearingSystemIdentification2ChoiceAuth02200104(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 5,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ContractBalanceType1ChoiceAuth02200104(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ContractClosureReason1ChoiceAuth02200104(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DateAndPlaceOfBirth1Auth02200104(ISO20022MessageElement):
    birth_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "BirthDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
        },
    )
    prvc_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrvcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    city_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "CityOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class DatePeriod3Auth02200104(ISO20022MessageElement):
    fr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
        },
    )
    to_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )


@dataclass
class DocumentAmendment1Auth02200104(ISO20022MessageElement):
    crrctn_id: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CrrctnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    orgnl_doc_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrgnlDocId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DocumentIdentification22Auth02200104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    dt_of_isse: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DtOfIsse",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )


@dataclass
class DocumentIdentification28Auth02200104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dt_of_isse: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DtOfIsse",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
        },
    )


@dataclass
class DocumentIdentification29Auth02200104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    dt_of_isse: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DtOfIsse",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
        },
    )


@dataclass
class DocumentIdentification35Auth02200104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dt_of_isse: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DtOfIsse",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )


@dataclass
class FinancialIdentificationSchemeName1ChoiceAuth02200104(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification30Auth02200104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class InterestPaymentDateRange1Auth02200104(ISO20022MessageElement):
    intrst_schdl_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "IntrstSchdlId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    xpctd_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "XpctdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    due_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DueDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )


@dataclass
class LegalOrganisation2Auth02200104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    estblishmt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EstblishmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    regn_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "RegnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )


@dataclass
class OrganisationIdentificationSchemeName1ChoiceAuth02200104(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class OtherContact1Auth02200104(ISO20022MessageElement):
    chanl_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChanlTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 4,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 128,
        },
    )


@dataclass
class PersonIdentificationSchemeName1ChoiceAuth02200104(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ProprietaryReference1Auth02200104(ISO20022MessageElement):
    tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ProxyAccountType1ChoiceAuth02200104(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ShipmentCondition1ChoiceAuth02200104(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ShipmentDateRange1Auth02200104(ISO20022MessageElement):
    earlst_shipmnt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EarlstShipmntDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    latst_shipmnt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "LatstShipmntDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )


@dataclass
class ShipmentDateRange2Auth02200104(ISO20022MessageElement):
    sub_qty_val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "SubQtyVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 17,
        },
    )
    earlst_shipmnt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EarlstShipmntDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    latst_shipmnt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "LatstShipmntDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )


@dataclass
class SignatureEnvelopeReferenceAuth02200104(ISO20022MessageElement):
    w3_org_2000_09_xmldsig_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )


@dataclass
class SupplementaryDataEnvelope1Auth02200104(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class TimePeriod2Auth02200104(ISO20022MessageElement):
    fr_tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "FrTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
        },
    )
    to_tm: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "ToTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )


@dataclass
class ValidationRuleSchemeName1ChoiceAuth02200104(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AddressType3ChoiceAuth02200104(ISO20022MessageElement):
    cd: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Auth02200104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )


@dataclass
class BenchmarkCurveName4ChoiceAuth02200104(ISO20022MessageElement):
    isin: Optional[str] = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    indx: Optional[BenchmarkCurveName2Code] = field(
        default=None,
        metadata={
            "name": "Indx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 25,
        },
    )


@dataclass
class CertificateIdentification1Auth02200104(ISO20022MessageElement):
    msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    acct_svcr_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcctSvcrRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    pmt_inf_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PmtInfId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    instr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "InstrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    end_to_end_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "EndToEndId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prtry: Optional[ProprietaryReference1Auth02200104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )


@dataclass
class ClearingSystemMemberIdentification2Auth02200104(ISO20022MessageElement):
    clr_sys_id: Optional[ClearingSystemIdentification2ChoiceAuth02200104] = field(
        default=None,
        metadata={
            "name": "ClrSysId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    mmb_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MmbId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Contact13Auth02200104(ISO20022MessageElement):
    nm_prfx: Optional[NamePrefix2Code] = field(
        default=None,
        metadata={
            "name": "NmPrfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    phne_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PhneNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    mob_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "MobNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    fax_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "FaxNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    urladr: Optional[str] = field(
        default=None,
        metadata={
            "name": "URLAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 2048,
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 256,
        },
    )
    email_purp: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailPurp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    job_titl: Optional[str] = field(
        default=None,
        metadata={
            "name": "JobTitl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rspnsblty: Optional[str] = field(
        default=None,
        metadata={
            "name": "Rspnsblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    othr: list[OtherContact1Auth02200104] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    prefrd_mtd: Optional[PreferredContactMethod2Code] = field(
        default=None,
        metadata={
            "name": "PrefrdMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )


@dataclass
class ContractBalance1Auth02200104(ISO20022MessageElement):
    tp: Optional[ContractBalanceType1ChoiceAuth02200104] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
        },
    )
    amt: Optional[ActiveCurrencyAndAmountAuth02200104] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
        },
    )
    cdt_dbt_ind: Optional[CreditDebit3Code] = field(
        default=None,
        metadata={
            "name": "CdtDbtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
        },
    )


@dataclass
class ContractRegistrationReference2ChoiceAuth02200104(ISO20022MessageElement):
    regd_ctrct_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegdCtrctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctrct: Optional[DocumentIdentification35Auth02200104] = field(
        default=None,
        metadata={
            "name": "Ctrct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )


@dataclass
class DocumentEntryAmendment1Auth02200104(ISO20022MessageElement):
    crrctg_ntry_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CrrctgNtryNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    orgnl_doc: Optional[DocumentIdentification28Auth02200104] = field(
        default=None,
        metadata={
            "name": "OrgnlDoc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
        },
    )


@dataclass
class DocumentGeneralInformation5Auth02200104(ISO20022MessageElement):
    doc_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "DocTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 4,
        },
    )
    doc_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "DocNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    doc_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "DocNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    sndr_rcvr_seq_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SndrRcvrSeqId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    isse_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "IsseDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "name": "URL",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 256,
        },
    )
    lk_file_hash: Optional[SignatureEnvelopeReferenceAuth02200104] = field(
        default=None,
        metadata={
            "name": "LkFileHash",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    attchd_binry_file: Optional[BinaryFile1Auth02200104] = field(
        default=None,
        metadata={
            "name": "AttchdBinryFile",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
        },
    )


@dataclass
class ExchangeRate1Auth02200104(ISO20022MessageElement):
    unit_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "XchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    rate_tp: Optional[ExchangeRateType1Code] = field(
        default=None,
        metadata={
            "name": "RateTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    ctrct_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericAccountIdentification1Auth02200104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 34,
        },
    )
    schme_nm: Optional[AccountSchemeName1ChoiceAuth02200104] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericFinancialIdentification1Auth02200104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[FinancialIdentificationSchemeName1ChoiceAuth02200104] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericOrganisationIdentification3Auth02200104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        },
    )
    schme_nm: Optional[OrganisationIdentificationSchemeName1ChoiceAuth02200104] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericPersonIdentification2Auth02200104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        },
    )
    schme_nm: Optional[PersonIdentificationSchemeName1ChoiceAuth02200104] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericValidationRuleIdentification1Auth02200104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    desc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )
    schme_nm: Optional[ValidationRuleSchemeName1ChoiceAuth02200104] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class InterestPaymentSchedule1Auth02200104(ISO20022MessageElement):
    intrst_schdl_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "IntrstSchdlId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    amt: Optional[ActiveCurrencyAndAmountAuth02200104] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    xpctd_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "XpctdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    due_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DueDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 1025,
        },
    )


@dataclass
class InterestRateContractTerm1Auth02200104(ISO20022MessageElement):
    unit: Optional[RateBasis1Code] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
        },
    )
    val: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )


@dataclass
class LoanContractTranche1Auth02200104(ISO20022MessageElement):
    trch_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TrchNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    xpctd_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "XpctdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
        },
    )
    amt: Optional[ActiveCurrencyAndAmountAuth02200104] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
        },
    )
    due_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DueDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    drtn_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "DrtnCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "pattern": r"[0-9]",
        },
    )
    last_trch_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LastTrchInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )


@dataclass
class PaymentSchedule1Auth02200104(ISO20022MessageElement):
    pmt_schdl_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PmtSchdlId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    amt: Optional[ActiveCurrencyAndAmountAuth02200104] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    xpctd_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "XpctdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    due_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DueDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 1025,
        },
    )


@dataclass
class PaymentScheduleType2ChoiceAuth02200104(ISO20022MessageElement):
    cd: Optional[PaymentScheduleType2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ProxyAccountIdentification1Auth02200104(ISO20022MessageElement):
    tp: Optional[ProxyAccountType1ChoiceAuth02200104] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 2048,
        },
    )


@dataclass
class RegisteredContractAmendment1Auth02200104(ISO20022MessageElement):
    amdmnt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "AmdmntDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
        },
    )
    doc: Optional[DocumentIdentification28Auth02200104] = field(
        default=None,
        metadata={
            "name": "Doc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
        },
    )
    start_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StartDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    amdmnt_rsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "AmdmntRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 1025,
        },
    )


@dataclass
class RegisteredContractCommunication1Auth02200104(ISO20022MessageElement):
    mtd: Optional[CommunicationMethod4Code] = field(
        default=None,
        metadata={
            "name": "Mtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
        },
    )
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
        },
    )


@dataclass
class ReportingPeriod4Auth02200104(ISO20022MessageElement):
    fr_to_dt: Optional[DatePeriod3Auth02200104] = field(
        default=None,
        metadata={
            "name": "FrToDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
        },
    )
    fr_to_tm: Optional[TimePeriod2Auth02200104] = field(
        default=None,
        metadata={
            "name": "FrToTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
        },
    )
    tp: Optional[QueryType3Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
        },
    )


@dataclass
class ShipmentAttribute2Auth02200104(ISO20022MessageElement):
    conds: Optional[ShipmentCondition1ChoiceAuth02200104] = field(
        default=None,
        metadata={
            "name": "Conds",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    xpctd_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "XpctdDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    ctry_of_cntr_pty: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfCntrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class ShipmentSchedule2ChoiceAuth02200104(ISO20022MessageElement):
    shipmnt_dt_rg: Optional[ShipmentDateRange1Auth02200104] = field(
        default=None,
        metadata={
            "name": "ShipmntDtRg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    shipmnt_sub_schdl: list[ShipmentDateRange2Auth02200104] = field(
        default_factory=list,
        metadata={
            "name": "ShipmntSubSchdl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )


@dataclass
class SpecialCondition1Auth02200104(ISO20022MessageElement):
    incmg_amt: Optional[ActiveCurrencyAndAmountAuth02200104] = field(
        default=None,
        metadata={
            "name": "IncmgAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
        },
    )
    outgng_amt: Optional[ActiveCurrencyAndAmountAuth02200104] = field(
        default=None,
        metadata={
            "name": "OutgngAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
        },
    )
    incmg_amt_to_othr_acct: Optional[ActiveCurrencyAndAmountAuth02200104] = field(
        default=None,
        metadata={
            "name": "IncmgAmtToOthrAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    pmt_fr_othr_acct: Optional[ActiveCurrencyAndAmountAuth02200104] = field(
        default=None,
        metadata={
            "name": "PmtFrOthrAcct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )


@dataclass
class SupplementaryData1Auth02200104(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Auth02200104] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
        },
    )


@dataclass
class TaxExemptionReasonFormat1ChoiceAuth02200104(ISO20022MessageElement):
    ustrd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ustrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    strd: Optional[TaxExemptReason1Code] = field(
        default=None,
        metadata={
            "name": "Strd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )


@dataclass
class AccountIdentification4ChoiceAuth02200104(ISO20022MessageElement):
    iban: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "pattern": r"[A-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}",
        },
    )
    othr: Optional[GenericAccountIdentification1Auth02200104] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )


@dataclass
class CertificateReference2Auth02200104(ISO20022MessageElement):
    id: Optional[CertificateIdentification1Auth02200104] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
        },
    )
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )


@dataclass
class FloatingInterestRate4Auth02200104(ISO20022MessageElement):
    ref_rate: Optional[BenchmarkCurveName4ChoiceAuth02200104] = field(
        default=None,
        metadata={
            "name": "RefRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
        },
    )
    term: Optional[InterestRateContractTerm1Auth02200104] = field(
        default=None,
        metadata={
            "name": "Term",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
        },
    )
    bsis_pt_sprd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "BsisPtSprd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )


@dataclass
class OrganisationIdentification39Auth02200104(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    othr: list[GenericOrganisationIdentification3Auth02200104] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )


@dataclass
class PersonIdentification18Auth02200104(ISO20022MessageElement):
    dt_and_plc_of_birth: Optional[DateAndPlaceOfBirth1Auth02200104] = field(
        default=None,
        metadata={
            "name": "DtAndPlcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    othr: list[GenericPersonIdentification2Auth02200104] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )


@dataclass
class PostalAddress27Auth02200104(ISO20022MessageElement):
    adr_tp: Optional[AddressType3ChoiceAuth02200104] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    care_of: Optional[str] = field(
        default=None,
        metadata={
            "name": "CareOf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    sub_dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubDept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    strt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 16,
        },
    )
    bldg_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    flr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Flr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    unit_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_bx: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstBx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 16,
        },
    )
    room: Optional[str] = field(
        default=None,
        metadata={
            "name": "Room",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    twn_lctn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnLctnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    dstrct_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "DstrctNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "max_occurs": 7,
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class SupportingDocumentEntry2Auth02200104(ISO20022MessageElement):
    ntry_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "NtryId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    orgnl_doc: Optional[DocumentIdentification22Auth02200104] = field(
        default=None,
        metadata={
            "name": "OrgnlDoc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
        },
    )
    doc_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "DocTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{1}[a-zA-Z0-9_]{3}",
        },
    )
    ttl_amt: Optional[ActiveCurrencyAndAmountAuth02200104] = field(
        default=None,
        metadata={
            "name": "TtlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    ttl_amt_aftr_shipmnt: Optional[ActiveCurrencyAndAmountAuth02200104] = field(
        default=None,
        metadata={
            "name": "TtlAmtAftrShipmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    ttl_amt_in_ctrct_ccy: Optional[ActiveCurrencyAndAmountAuth02200104] = field(
        default=None,
        metadata={
            "name": "TtlAmtInCtrctCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    ttl_amt_aftr_shipmnt_in_ctrct_ccy: Optional[ActiveCurrencyAndAmountAuth02200104] = (
        field(
            default=None,
            metadata={
                "name": "TtlAmtAftrShipmntInCtrctCcy",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            },
        )
    )
    shipmnt_attrbts: Optional[ShipmentAttribute2Auth02200104] = field(
        default=None,
        metadata={
            "name": "ShipmntAttrbts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
        },
    )
    ntry_amdmnt_id: Optional[DocumentEntryAmendment1Auth02200104] = field(
        default=None,
        metadata={
            "name": "NtryAmdmntId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    mtrty_data: Optional[str] = field(
        default=None,
        metadata={
            "name": "MtrtyData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 500,
        },
    )
    attchmnt: list[DocumentGeneralInformation5Auth02200104] = field(
        default_factory=list,
        metadata={
            "name": "Attchmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )


@dataclass
class TaxParty4Auth02200104(ISO20022MessageElement):
    tax_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tax_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    regn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tax_xmptn_rsn: list[TaxExemptionReasonFormat1ChoiceAuth02200104] = field(
        default_factory=list,
        metadata={
            "name": "TaxXmptnRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )


@dataclass
class TransactionCertificateContract2Auth02200104(ISO20022MessageElement):
    ctrct_ref: Optional[ContractRegistrationReference2ChoiceAuth02200104] = field(
        default=None,
        metadata={
            "name": "CtrctRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    tx_amt_in_ctrct_ccy: Optional[ActiveCurrencyAndAmountAuth02200104] = field(
        default=None,
        metadata={
            "name": "TxAmtInCtrctCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    xpctd_shipmnt_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "XpctdShipmntDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    xpctd_advnc_pmt_rtr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "XpctdAdvncPmtRtrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 1025,
        },
    )


@dataclass
class BranchData5Auth02200104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress27Auth02200104] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )


@dataclass
class CashAccount40Auth02200104(ISO20022MessageElement):
    id: Optional[AccountIdentification4ChoiceAuth02200104] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    tp: Optional[CashAccountType2ChoiceAuth02200104] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    prxy: Optional[ProxyAccountIdentification1Auth02200104] = field(
        default=None,
        metadata={
            "name": "Prxy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )


@dataclass
class CashCollateral5Auth02200104(ISO20022MessageElement):
    coll_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CollId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    csh_acct_id: Optional[AccountIdentification4ChoiceAuth02200104] = field(
        default=None,
        metadata={
            "name": "CshAcctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    asst_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "AsstNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dpst_amt: Optional[ActiveCurrencyAndAmountAuth02200104] = field(
        default=None,
        metadata={
            "name": "DpstAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    dpst_tp: Optional[DepositType1Code] = field(
        default=None,
        metadata={
            "name": "DpstTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    mtrty_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "MtrtyDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    val_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ValDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    xchg_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "XchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    coll_val: Optional[ActiveCurrencyAndAmountAuth02200104] = field(
        default=None,
        metadata={
            "name": "CollVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
        },
    )
    hrcut: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Hrcut",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass
class FinancialInstitutionIdentification23Auth02200104(ISO20022MessageElement):
    bicfi: Optional[str] = field(
        default=None,
        metadata={
            "name": "BICFI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    clr_sys_mmb_id: Optional[ClearingSystemMemberIdentification2Auth02200104] = field(
        default=None,
        metadata={
            "name": "ClrSysMmbId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress27Auth02200104] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    othr: Optional[GenericFinancialIdentification1Auth02200104] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )


@dataclass
class InterestRate2ChoiceAuth02200104(ISO20022MessageElement):
    fxd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Fxd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    fltg: Optional[FloatingInterestRate4Auth02200104] = field(
        default=None,
        metadata={
            "name": "Fltg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )


@dataclass
class Party52ChoiceAuth02200104(ISO20022MessageElement):
    org_id: Optional[OrganisationIdentification39Auth02200104] = field(
        default=None,
        metadata={
            "name": "OrgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    prvt_id: Optional[PersonIdentification18Auth02200104] = field(
        default=None,
        metadata={
            "name": "PrvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )


@dataclass
class TransactionCertificate5Auth02200104(ISO20022MessageElement):
    rfrd_doc: Optional[CertificateReference2Auth02200104] = field(
        default=None,
        metadata={
            "name": "RfrdDoc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
        },
    )
    tx_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "TxDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
        },
    )
    tx_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "pattern": r"[0-9]",
        },
    )
    lcl_instrm: Optional[str] = field(
        default=None,
        metadata={
            "name": "LclInstrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
            "pattern": r"[0-9]{5}",
        },
    )
    amt: Optional[ActiveCurrencyAndAmountAuth02200104] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
        },
    )


@dataclass
class BranchAndFinancialInstitutionIdentification8Auth02200104(ISO20022MessageElement):
    fin_instn_id: Optional[FinancialInstitutionIdentification23Auth02200104] = field(
        default=None,
        metadata={
            "name": "FinInstnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
        },
    )
    brnch_id: Optional[BranchData5Auth02200104] = field(
        default=None,
        metadata={
            "name": "BrnchId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )


@dataclass
class ContractCollateral1Auth02200104(ISO20022MessageElement):
    ttl_amt: Optional[ActiveCurrencyAndAmountAuth02200104] = field(
        default=None,
        metadata={
            "name": "TtlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
        },
    )
    coll_desc: list[CashCollateral5Auth02200104] = field(
        default_factory=list,
        metadata={
            "name": "CollDesc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 1025,
        },
    )


@dataclass
class PartyIdentification272Auth02200104(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress27Auth02200104] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    id: Optional[Party52ChoiceAuth02200104] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    ctry_of_res: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfRes",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    ctct_dtls: Optional[Contact13Auth02200104] = field(
        default=None,
        metadata={
            "name": "CtctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )


@dataclass
class TransactionCertificateRecord2Auth02200104(ISO20022MessageElement):
    cert_rcrd_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CertRcrdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    doc_submitg_prcdr: Optional[str] = field(
        default=None,
        metadata={
            "name": "DocSubmitgPrcdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "pattern": r"[0-9]",
        },
    )
    tx: Optional[TransactionCertificate5Auth02200104] = field(
        default=None,
        metadata={
            "name": "Tx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
        },
    )
    ctrct: Optional[TransactionCertificateContract2Auth02200104] = field(
        default=None,
        metadata={
            "name": "Ctrct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    attchmnt: list[DocumentGeneralInformation5Auth02200104] = field(
        default_factory=list,
        metadata={
            "name": "Attchmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )


@dataclass
class CurrencyControlHeader7Auth02200104(ISO20022MessageElement):
    msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    cre_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
        },
    )
    nb_of_itms: Optional[str] = field(
        default=None,
        metadata={
            "name": "NbOfItms",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
            "pattern": r"[0-9]{1,15}",
        },
    )
    rcvg_pty: Optional[PartyIdentification272Auth02200104] = field(
        default=None,
        metadata={
            "name": "RcvgPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
        },
    )
    regn_agt: Optional[BranchAndFinancialInstitutionIdentification8Auth02200104] = (
        field(
            default=None,
            metadata={
                "name": "RegnAgt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
                "required": True,
            },
        )
    )


@dataclass
class RegisteredContractJournal3Auth02200104(ISO20022MessageElement):
    regn_agt: Optional[BranchAndFinancialInstitutionIdentification8Auth02200104] = (
        field(
            default=None,
            metadata={
                "name": "RegnAgt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
                "required": True,
            },
        )
    )
    unq_id: Optional[DocumentIdentification28Auth02200104] = field(
        default=None,
        metadata={
            "name": "UnqId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    clsr_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ClsrDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
        },
    )
    clsr_rsn: Optional[ContractClosureReason1ChoiceAuth02200104] = field(
        default=None,
        metadata={
            "name": "ClsrRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
        },
    )


@dataclass
class SupportingDocument4Auth02200104(ISO20022MessageElement):
    spprtg_doc_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SpprtgDocId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    orgnl_req_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrgnlReqId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cert: Optional[DocumentIdentification28Auth02200104] = field(
        default=None,
        metadata={
            "name": "Cert",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
        },
    )
    acct_ownr: Optional[PartyIdentification272Auth02200104] = field(
        default=None,
        metadata={
            "name": "AcctOwnr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
        },
    )
    acct_svcr: Optional[BranchAndFinancialInstitutionIdentification8Auth02200104] = (
        field(
            default=None,
            metadata={
                "name": "AcctSvcr",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
                "required": True,
            },
        )
    )
    amdmnt: Optional[DocumentAmendment1Auth02200104] = field(
        default=None,
        metadata={
            "name": "Amdmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    ctrct_ref: Optional[ContractRegistrationReference2ChoiceAuth02200104] = field(
        default=None,
        metadata={
            "name": "CtrctRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
        },
    )
    ntry: list[SupportingDocumentEntry2Auth02200104] = field(
        default_factory=list,
        metadata={
            "name": "Ntry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_occurs": 1,
        },
    )
    splmtry_data: list[SupplementaryData1Auth02200104] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )


@dataclass
class TradeParty6Auth02200104(ISO20022MessageElement):
    pty_id: Optional[PartyIdentification272Auth02200104] = field(
        default=None,
        metadata={
            "name": "PtyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
        },
    )
    lgl_org: Optional[LegalOrganisation2Auth02200104] = field(
        default=None,
        metadata={
            "name": "LglOrg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    tax_pty: list[TaxParty4Auth02200104] = field(
        default_factory=list,
        metadata={
            "name": "TaxPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )


@dataclass
class TransactionCertificate4Auth02200104(ISO20022MessageElement):
    tx_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    cert: Optional[DocumentIdentification28Auth02200104] = field(
        default=None,
        metadata={
            "name": "Cert",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
        },
    )
    acct: Optional[CashAccount40Auth02200104] = field(
        default=None,
        metadata={
            "name": "Acct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    bk_acct_dmcltn_ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "BkAcctDmcltnCtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    amdmnt: Optional[DocumentAmendment1Auth02200104] = field(
        default=None,
        metadata={
            "name": "Amdmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    cert_rcrd: list[TransactionCertificateRecord2Auth02200104] = field(
        default_factory=list,
        metadata={
            "name": "CertRcrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_occurs": 1,
        },
    )
    splmtry_data: list[SupplementaryData1Auth02200104] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )


@dataclass
class SyndicatedLoan3Auth02200104(ISO20022MessageElement):
    brrwr: Optional[TradeParty6Auth02200104] = field(
        default=None,
        metadata={
            "name": "Brrwr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
        },
    )
    lndr: Optional[TradeParty6Auth02200104] = field(
        default=None,
        metadata={
            "name": "Lndr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    amt: Optional[ActiveCurrencyAndAmountAuth02200104] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    shr: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Shr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    xchg_rate_inf: Optional[ExchangeRate1Auth02200104] = field(
        default=None,
        metadata={
            "name": "XchgRateInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )


@dataclass
class TradeContract4Auth02200104(ISO20022MessageElement):
    ctrct_doc_id: Optional[DocumentIdentification22Auth02200104] = field(
        default=None,
        metadata={
            "name": "CtrctDocId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    trad_tp_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TradTpId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    amt: Optional[ActiveCurrencyAndAmountAuth02200104] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    buyr: list[TradeParty6Auth02200104] = field(
        default_factory=list,
        metadata={
            "name": "Buyr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_occurs": 1,
        },
    )
    sellr: list[TradeParty6Auth02200104] = field(
        default_factory=list,
        metadata={
            "name": "Sellr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_occurs": 1,
        },
    )
    mtrty_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "MtrtyDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    prlngtn_flg: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PrlngtnFlg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    start_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StartDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    sttlm_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "SttlmCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    xchg_rate_inf: Optional[ExchangeRate1Auth02200104] = field(
        default=None,
        metadata={
            "name": "XchgRateInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    pmt_schdl: Optional[InterestPaymentDateRange1Auth02200104] = field(
        default=None,
        metadata={
            "name": "PmtSchdl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    shipmnt_schdl: Optional[ShipmentSchedule2ChoiceAuth02200104] = field(
        default=None,
        metadata={
            "name": "ShipmntSchdl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    attchmnt: list[DocumentGeneralInformation5Auth02200104] = field(
        default_factory=list,
        metadata={
            "name": "Attchmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )


@dataclass
class LoanContract4Auth02200104(ISO20022MessageElement):
    ctrct_doc_id: Optional[DocumentIdentification22Auth02200104] = field(
        default=None,
        metadata={
            "name": "CtrctDocId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
        },
    )
    ln_tp_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LnTpId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    buyr: list[TradeParty6Auth02200104] = field(
        default_factory=list,
        metadata={
            "name": "Buyr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_occurs": 1,
        },
    )
    sellr: list[TradeParty6Auth02200104] = field(
        default_factory=list,
        metadata={
            "name": "Sellr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_occurs": 1,
        },
    )
    amt: Optional[ActiveCurrencyAndAmountAuth02200104] = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    mtrty_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "MtrtyDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    prlngtn_flg: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PrlngtnFlg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    start_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StartDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    sttlm_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "SttlmCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "pattern": r"[A-Z]{3,3}",
        },
    )
    spcl_conds: Optional[SpecialCondition1Auth02200104] = field(
        default=None,
        metadata={
            "name": "SpclConds",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    drtn_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "DrtnCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "pattern": r"[0-9]",
        },
    )
    intrst_rate: Optional[InterestRate2ChoiceAuth02200104] = field(
        default=None,
        metadata={
            "name": "IntrstRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    trch: list[LoanContractTranche1Auth02200104] = field(
        default_factory=list,
        metadata={
            "name": "Trch",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    pmt_schdl: list[PaymentSchedule1Auth02200104] = field(
        default_factory=list,
        metadata={
            "name": "PmtSchdl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    intrst_schdl: list[InterestPaymentSchedule1Auth02200104] = field(
        default_factory=list,
        metadata={
            "name": "IntrstSchdl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    intra_cpny_ln: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IntraCpnyLn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
        },
    )
    coll: Optional[ContractCollateral1Auth02200104] = field(
        default=None,
        metadata={
            "name": "Coll",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    sndctd_ln: list[SyndicatedLoan3Auth02200104] = field(
        default_factory=list,
        metadata={
            "name": "SndctdLn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    attchmnt: list[DocumentGeneralInformation5Auth02200104] = field(
        default_factory=list,
        metadata={
            "name": "Attchmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )


@dataclass
class UnderlyingContract4ChoiceAuth02200104(ISO20022MessageElement):
    ln: Optional[LoanContract4Auth02200104] = field(
        default=None,
        metadata={
            "name": "Ln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    trad: Optional[TradeContract4Auth02200104] = field(
        default=None,
        metadata={
            "name": "Trad",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )


@dataclass
class RegisteredContract18Auth02200104(ISO20022MessageElement):
    orgnl_ctrct_regn_req: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrgnlCtrctRegnReq",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr_fi: Optional[BranchAndFinancialInstitutionIdentification8Auth02200104] = field(
        default=None,
        metadata={
            "name": "IssrFI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
        },
    )
    ctrct: Optional[UnderlyingContract4ChoiceAuth02200104] = field(
        default=None,
        metadata={
            "name": "Ctrct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
        },
    )
    ctrct_bal: list[ContractBalance1Auth02200104] = field(
        default_factory=list,
        metadata={
            "name": "CtrctBal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    pmt_schdl_tp: Optional[PaymentScheduleType2ChoiceAuth02200104] = field(
        default=None,
        metadata={
            "name": "PmtSchdlTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    regd_ctrct_id: Optional[DocumentIdentification29Auth02200104] = field(
        default=None,
        metadata={
            "name": "RegdCtrctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
        },
    )
    prvs_regd_ctrct_id: Optional[DocumentIdentification22Auth02200104] = field(
        default=None,
        metadata={
            "name": "PrvsRegdCtrctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    regd_ctrct_jrnl: list[RegisteredContractJournal3Auth02200104] = field(
        default_factory=list,
        metadata={
            "name": "RegdCtrctJrnl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    amdmnt: list[RegisteredContractAmendment1Auth02200104] = field(
        default_factory=list,
        metadata={
            "name": "Amdmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    submissn: Optional[RegisteredContractCommunication1Auth02200104] = field(
        default=None,
        metadata={
            "name": "Submissn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
        },
    )
    dlvry: Optional[RegisteredContractCommunication1Auth02200104] = field(
        default=None,
        metadata={
            "name": "Dlvry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
        },
    )
    ln_prncpl_amt: Optional[ActiveCurrencyAndAmountAuth02200104] = field(
        default=None,
        metadata={
            "name": "LnPrncplAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    estmtd_dt_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "EstmtdDtInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
        },
    )
    intr_cpny_ln: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IntrCpnyLn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
        },
    )
    addtl_inf: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 1025,
        },
    )


@dataclass
class ContractRegistrationStatement4Auth02200104(ISO20022MessageElement):
    stmt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "StmtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rptg_pty: Optional[TradeParty6Auth02200104] = field(
        default=None,
        metadata={
            "name": "RptgPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
        },
    )
    regn_agt: Optional[BranchAndFinancialInstitutionIdentification8Auth02200104] = (
        field(
            default=None,
            metadata={
                "name": "RegnAgt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
                "required": True,
            },
        )
    )
    rptg_prd: Optional[ReportingPeriod4Auth02200104] = field(
        default=None,
        metadata={
            "name": "RptgPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
        },
    )
    regd_ctrct: Optional[RegisteredContract18Auth02200104] = field(
        default=None,
        metadata={
            "name": "RegdCtrct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
        },
    )
    tx_jrnl: list[TransactionCertificate4Auth02200104] = field(
        default_factory=list,
        metadata={
            "name": "TxJrnl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    spprtg_doc_jrnl: list[SupportingDocument4Auth02200104] = field(
        default_factory=list,
        metadata={
            "name": "SpprtgDocJrnl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    addtl_spprtg_doc_jrnl: list[SupportingDocument4Auth02200104] = field(
        default_factory=list,
        metadata={
            "name": "AddtlSpprtgDocJrnl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    rgltry_rule_vldtn: list[GenericValidationRuleIdentification1Auth02200104] = field(
        default_factory=list,
        metadata={
            "name": "RgltryRuleVldtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )
    ttl_ctrct_trnvr_sum: Optional[ActiveCurrencyAndAmountAuth02200104] = field(
        default=None,
        metadata={
            "name": "TtlCtrctTrnvrSum",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
        },
    )
    splmtry_data: list[SupplementaryData1Auth02200104] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )


@dataclass
class ContractRegistrationStatementV04Auth02200104(ISO20022MessageElement):
    grp_hdr: Optional[CurrencyControlHeader7Auth02200104] = field(
        default=None,
        metadata={
            "name": "GrpHdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "required": True,
        },
    )
    stmt: list[ContractRegistrationStatement4Auth02200104] = field(
        default_factory=list,
        metadata={
            "name": "Stmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
            "min_occurs": 1,
        },
    )
    splmtry_data: list[SupplementaryData1Auth02200104] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04",
        },
    )


@dataclass
class Auth02200104(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:auth.022.001.04"

    ctrct_regn_stmt: Optional[ContractRegistrationStatementV04Auth02200104] = field(
        default=None,
        metadata={
            "name": "CtrctRegnStmt",
            "type": "Element",
            "required": True,
        },
    )
