from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import (
    AddressType2Code,
    NamePrefix2Code,
    PreferredContactMethod2Code,
)
from python_iso20022.reda.enums import ServiceRequestStatus1Code

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02"


@dataclass
class DateAndDateTime2ChoiceReda07300102(ISO20022MessageElement):
    dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Dt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
        },
    )
    dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
        },
    )


@dataclass
class DateAndPlaceOfBirth1Reda07300102(ISO20022MessageElement):
    birth_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "BirthDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
            "required": True,
        },
    )
    prvc_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrvcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    city_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "CityOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class DebtorActivationStatusReason1ChoiceReda07300102(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification1Reda07300102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification30Reda07300102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class OrganisationIdentificationSchemeName1ChoiceReda07300102(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class OriginalBusinessInstruction1Reda07300102(ISO20022MessageElement):
    msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    msg_nm_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgNmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cre_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
        },
    )


@dataclass
class OtherContact1Reda07300102(ISO20022MessageElement):
    chanl_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChanlTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
            "min_length": 1,
            "max_length": 128,
        },
    )


@dataclass
class PersonIdentificationSchemeName1ChoiceReda07300102(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryDataEnvelope1Reda07300102(ISO20022MessageElement):
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class AddressType3ChoiceReda07300102(ISO20022MessageElement):
    cd: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
        },
    )
    prtry: Optional[GenericIdentification30Reda07300102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
        },
    )


@dataclass
class Contact13Reda07300102(ISO20022MessageElement):
    nm_prfx: Optional[NamePrefix2Code] = field(
        default=None,
        metadata={
            "name": "NmPrfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
            "min_length": 1,
            "max_length": 140,
        },
    )
    phne_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PhneNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    mob_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "MobNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    fax_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "FaxNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    urladr: Optional[str] = field(
        default=None,
        metadata={
            "name": "URLAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
            "min_length": 1,
            "max_length": 2048,
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
            "min_length": 1,
            "max_length": 256,
        },
    )
    email_purp: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailPurp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    job_titl: Optional[str] = field(
        default=None,
        metadata={
            "name": "JobTitl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rspnsblty: Optional[str] = field(
        default=None,
        metadata={
            "name": "Rspnsblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
            "min_length": 1,
            "max_length": 70,
        },
    )
    othr: list[OtherContact1Reda07300102] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
        },
    )
    prefrd_mtd: Optional[PreferredContactMethod2Code] = field(
        default=None,
        metadata={
            "name": "PrefrdMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
        },
    )


@dataclass
class DocumentFormat2ChoiceReda07300102(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[GenericIdentification1Reda07300102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
        },
    )


@dataclass
class DocumentType1ChoiceReda07300102(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[GenericIdentification1Reda07300102] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
        },
    )


@dataclass
class GenericOrganisationIdentification3Reda07300102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        },
    )
    schme_nm: Optional[OrganisationIdentificationSchemeName1ChoiceReda07300102] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericPersonIdentification2Reda07300102(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        },
    )
    schme_nm: Optional[PersonIdentificationSchemeName1ChoiceReda07300102] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ServiceStatus1ChoiceReda07300102(ISO20022MessageElement):
    cd: Optional[ServiceRequestStatus1Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SupplementaryData1Reda07300102(ISO20022MessageElement):
    plc_and_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: Optional[SupplementaryDataEnvelope1Reda07300102] = field(
        default=None,
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
            "required": True,
        },
    )


@dataclass
class ContractReference1Reda07300102(ISO20022MessageElement):
    tp: Optional[DocumentType1ChoiceReda07300102] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
        },
    )
    ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ref",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
            "required": True,
            "min_length": 1,
            "max_length": 500,
        },
    )


@dataclass
class OrganisationIdentification40Reda07300102(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
            "min_length": 1,
            "max_length": 256,
        },
    )
    othr: list[GenericOrganisationIdentification3Reda07300102] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
        },
    )


@dataclass
class PersonIdentification20Reda07300102(ISO20022MessageElement):
    dt_and_plc_of_birth: Optional[DateAndPlaceOfBirth1Reda07300102] = field(
        default=None,
        metadata={
            "name": "DtAndPlcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
            "min_length": 1,
            "max_length": 256,
        },
    )
    othr: list[GenericPersonIdentification2Reda07300102] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
        },
    )


@dataclass
class PostalAddress27Reda07300102(ISO20022MessageElement):
    adr_tp: Optional[AddressType3ChoiceReda07300102] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
        },
    )
    care_of: Optional[str] = field(
        default=None,
        metadata={
            "name": "CareOf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
            "min_length": 1,
            "max_length": 140,
        },
    )
    dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
            "min_length": 1,
            "max_length": 70,
        },
    )
    sub_dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubDept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
            "min_length": 1,
            "max_length": 70,
        },
    )
    strt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
            "min_length": 1,
            "max_length": 140,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
            "min_length": 1,
            "max_length": 16,
        },
    )
    bldg_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
            "min_length": 1,
            "max_length": 140,
        },
    )
    flr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Flr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
            "min_length": 1,
            "max_length": 70,
        },
    )
    unit_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_bx: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstBx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
            "min_length": 1,
            "max_length": 16,
        },
    )
    room: Optional[str] = field(
        default=None,
        metadata={
            "name": "Room",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
            "min_length": 1,
            "max_length": 70,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
            "min_length": 1,
            "max_length": 140,
        },
    )
    twn_lctn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnLctnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
            "min_length": 1,
            "max_length": 140,
        },
    )
    dstrct_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "DstrctNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
            "min_length": 1,
            "max_length": 140,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
            "max_occurs": 7,
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class Party53ChoiceReda07300102(ISO20022MessageElement):
    org_id: Optional[OrganisationIdentification40Reda07300102] = field(
        default=None,
        metadata={
            "name": "OrgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
        },
    )
    prvt_id: Optional[PersonIdentification20Reda07300102] = field(
        default=None,
        metadata={
            "name": "PrvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
        },
    )


@dataclass
class RtppartyIdentification2Reda07300102(ISO20022MessageElement):
    class Meta:
        name = "RTPPartyIdentification2"

    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress27Reda07300102] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
        },
    )
    id: Optional[Party53ChoiceReda07300102] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
        },
    )
    ctry_of_res: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfRes",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    ctct_dtls: Optional[Contact13Reda07300102] = field(
        default=None,
        metadata={
            "name": "CtctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
        },
    )


@dataclass
class ActivationHeader3Reda07300102(ISO20022MessageElement):
    msg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
            "required": True,
        },
    )
    msg_orgtr: Optional[RtppartyIdentification2Reda07300102] = field(
        default=None,
        metadata={
            "name": "MsgOrgtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
        },
    )
    msg_rcpt: Optional[RtppartyIdentification2Reda07300102] = field(
        default=None,
        metadata={
            "name": "MsgRcpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
        },
    )
    initg_pty: Optional[RtppartyIdentification2Reda07300102] = field(
        default=None,
        metadata={
            "name": "InitgPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
            "required": True,
        },
    )


@dataclass
class DebtorActivation5Reda07300102(ISO20022MessageElement):
    dbtr_actvtn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "DbtrActvtnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )
    disp_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "DispNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
            "min_length": 1,
            "max_length": 140,
        },
    )
    ultmt_dbtr: Optional[RtppartyIdentification2Reda07300102] = field(
        default=None,
        metadata={
            "name": "UltmtDbtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
        },
    )
    dbtr: Optional[RtppartyIdentification2Reda07300102] = field(
        default=None,
        metadata={
            "name": "Dbtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
            "required": True,
        },
    )
    dbtr_sol_prvdr: Optional[RtppartyIdentification2Reda07300102] = field(
        default=None,
        metadata={
            "name": "DbtrSolPrvdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
            "required": True,
        },
    )
    cstmr_id: list[Party53ChoiceReda07300102] = field(
        default_factory=list,
        metadata={
            "name": "CstmrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
        },
    )
    ctrct_frmt_tp: list[DocumentFormat2ChoiceReda07300102] = field(
        default_factory=list,
        metadata={
            "name": "CtrctFrmtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
        },
    )
    ctrct_ref: list[ContractReference1Reda07300102] = field(
        default_factory=list,
        metadata={
            "name": "CtrctRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
        },
    )
    cdtr: Optional[RtppartyIdentification2Reda07300102] = field(
        default=None,
        metadata={
            "name": "Cdtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
            "required": True,
        },
    )
    ultmt_cdtr: Optional[RtppartyIdentification2Reda07300102] = field(
        default=None,
        metadata={
            "name": "UltmtCdtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
        },
    )
    actvtn_req_dlvry_pty: Optional[RtppartyIdentification2Reda07300102] = field(
        default=None,
        metadata={
            "name": "ActvtnReqDlvryPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
        },
    )
    start_dt: Optional[DateAndDateTime2ChoiceReda07300102] = field(
        default=None,
        metadata={
            "name": "StartDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
        },
    )
    end_dt: Optional[DateAndDateTime2ChoiceReda07300102] = field(
        default=None,
        metadata={
            "name": "EndDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
        },
    )
    ddctd_actvtn_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "DdctdActvtnCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DebtorActivationStatusReason3Reda07300102(ISO20022MessageElement):
    orgtr: Optional[RtppartyIdentification2Reda07300102] = field(
        default=None,
        metadata={
            "name": "Orgtr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
        },
    )
    rsn: Optional[DebtorActivationStatusReason1ChoiceReda07300102] = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
            "required": True,
        },
    )
    addtl_inf: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AddtlInf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
            "min_length": 1,
            "max_length": 105,
        },
    )


@dataclass
class OriginalActivation3ChoiceReda07300102(ISO20022MessageElement):
    orgnl_dbtr_id: Optional[Party53ChoiceReda07300102] = field(
        default=None,
        metadata={
            "name": "OrgnlDbtrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
        },
    )
    orgnl_actvtn_data: Optional[DebtorActivation5Reda07300102] = field(
        default=None,
        metadata={
            "name": "OrgnlActvtnData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
        },
    )


@dataclass
class ActivationStatus3Reda07300102(ISO20022MessageElement):
    orgnl_biz_instr: Optional[OriginalBusinessInstruction1Reda07300102] = field(
        default=None,
        metadata={
            "name": "OrgnlBizInstr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
        },
    )
    sts: Optional[ServiceStatus1ChoiceReda07300102] = field(
        default=None,
        metadata={
            "name": "Sts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
            "required": True,
        },
    )
    sts_rsn: Optional[DebtorActivationStatusReason3Reda07300102] = field(
        default=None,
        metadata={
            "name": "StsRsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
        },
    )
    orgnl_actvtn_ref: Optional[OriginalActivation3ChoiceReda07300102] = field(
        default=None,
        metadata={
            "name": "OrgnlActvtnRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
        },
    )
    fctv_actvtn_dt: Optional[DateAndDateTime2ChoiceReda07300102] = field(
        default=None,
        metadata={
            "name": "FctvActvtnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
        },
    )
    splmtry_data: list[SupplementaryData1Reda07300102] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
        },
    )


@dataclass
class RequestToPayDebtorActivationStatusReportV02Reda07300102(ISO20022MessageElement):
    hdr: Optional[ActivationHeader3Reda07300102] = field(
        default=None,
        metadata={
            "name": "Hdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
            "required": True,
        },
    )
    orgnl_actvtn_and_sts: list[ActivationStatus3Reda07300102] = field(
        default_factory=list,
        metadata={
            "name": "OrgnlActvtnAndSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
            "min_occurs": 1,
        },
    )
    splmtry_data: list[SupplementaryData1Reda07300102] = field(
        default_factory=list,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02",
        },
    )


@dataclass
class Reda07300102(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02"

    req_to_pay_dbtr_actvtn_sts_rpt: Optional[
        RequestToPayDebtorActivationStatusReportV02Reda07300102
    ] = field(
        default=None,
        metadata={
            "name": "ReqToPayDbtrActvtnStsRpt",
            "type": "Element",
            "required": True,
        },
    )
