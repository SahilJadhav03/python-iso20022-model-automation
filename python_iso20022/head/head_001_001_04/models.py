from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.enums import (
    AddressType2Code,
    CopyDuplicate1Code,
    NamePrefix2Code,
    PreferredContactMethod2Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:head.001.001.04"


@dataclass
class ClearingSystemIdentification2ChoiceHead00100104(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "min_length": 1,
            "max_length": 5,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DateAndPlaceOfBirth1Head00100104(ISO20022MessageElement):
    birth_dt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "BirthDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "required": True,
        },
    )
    prvc_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrvcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    city_of_birth: Optional[str] = field(
        default=None,
        metadata={
            "name": "CityOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass
class FinancialIdentificationSchemeName1ChoiceHead00100104(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericIdentification30Head00100104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{4}",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ImplementationSpecification1Head00100104(ISO20022MessageElement):
    regy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Regy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 350,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 2048,
        },
    )


@dataclass
class OrganisationIdentificationSchemeName1ChoiceHead00100104(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class OtherContact1Head00100104(ISO20022MessageElement):
    chanl_tp: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChanlTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
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
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "min_length": 1,
            "max_length": 128,
        },
    )


@dataclass
class PersonIdentificationSchemeName1ChoiceHead00100104(ISO20022MessageElement):
    cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "min_length": 1,
            "max_length": 4,
        },
    )
    prtry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class SignatureEnvelopeHead00100104(ISO20022MessageElement):
    w3_org_2000_09_xmldsig_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )


@dataclass
class AddressType3ChoiceHead00100104(ISO20022MessageElement):
    cd: Optional[AddressType2Code] = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
        },
    )
    prtry: Optional[GenericIdentification30Head00100104] = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
        },
    )


@dataclass
class ClearingSystemMemberIdentification2Head00100104(ISO20022MessageElement):
    clr_sys_id: Optional[ClearingSystemIdentification2ChoiceHead00100104] = field(
        default=None,
        metadata={
            "name": "ClrSysId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
        },
    )
    mmb_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MmbId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Contact13Head00100104(ISO20022MessageElement):
    nm_prfx: Optional[NamePrefix2Code] = field(
        default=None,
        metadata={
            "name": "NmPrfx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    phne_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "PhneNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    mob_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "MobNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    fax_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "FaxNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "pattern": r"\+[0-9]{1,3}-[0-9()+\-]{1,30}",
        },
    )
    urladr: Optional[str] = field(
        default=None,
        metadata={
            "name": "URLAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "min_length": 1,
            "max_length": 2048,
        },
    )
    email_adr: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "min_length": 1,
            "max_length": 256,
        },
    )
    email_purp: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailPurp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    job_titl: Optional[str] = field(
        default=None,
        metadata={
            "name": "JobTitl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    rspnsblty: Optional[str] = field(
        default=None,
        metadata={
            "name": "Rspnsblty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    othr: list[OtherContact1Head00100104] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
        },
    )
    prefrd_mtd: Optional[PreferredContactMethod2Code] = field(
        default=None,
        metadata={
            "name": "PrefrdMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
        },
    )


@dataclass
class GenericFinancialIdentification1Head00100104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    schme_nm: Optional[FinancialIdentificationSchemeName1ChoiceHead00100104] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericOrganisationIdentification3Head00100104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        },
    )
    schme_nm: Optional[OrganisationIdentificationSchemeName1ChoiceHead00100104] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GenericPersonIdentification2Head00100104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        },
    )
    schme_nm: Optional[PersonIdentificationSchemeName1ChoiceHead00100104] = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
        },
    )
    issr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class OrganisationIdentification39Head00100104(ISO20022MessageElement):
    any_bic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    othr: list[GenericOrganisationIdentification3Head00100104] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
        },
    )


@dataclass
class PersonIdentification18Head00100104(ISO20022MessageElement):
    dt_and_plc_of_birth: Optional[DateAndPlaceOfBirth1Head00100104] = field(
        default=None,
        metadata={
            "name": "DtAndPlcOfBirth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
        },
    )
    othr: list[GenericPersonIdentification2Head00100104] = field(
        default_factory=list,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
        },
    )


@dataclass
class PostalAddress27Head00100104(ISO20022MessageElement):
    adr_tp: Optional[AddressType3ChoiceHead00100104] = field(
        default=None,
        metadata={
            "name": "AdrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
        },
    )
    care_of: Optional[str] = field(
        default=None,
        metadata={
            "name": "CareOf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    sub_dept: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubDept",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    strt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "min_length": 1,
            "max_length": 16,
        },
    )
    bldg_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    flr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Flr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    unit_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnitNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_bx: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstBx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "min_length": 1,
            "max_length": 16,
        },
    )
    room: Optional[str] = field(
        default=None,
        metadata={
            "name": "Room",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "min_length": 1,
            "max_length": 70,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    twn_lctn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnLctnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    dstrct_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "DstrctNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    ctry_sub_dvsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "max_occurs": 7,
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class BranchData5Head00100104(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress27Head00100104] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
        },
    )


@dataclass
class FinancialInstitutionIdentification23Head00100104(ISO20022MessageElement):
    bicfi: Optional[str] = field(
        default=None,
        metadata={
            "name": "BICFI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )
    clr_sys_mmb_id: Optional[ClearingSystemMemberIdentification2Head00100104] = field(
        default=None,
        metadata={
            "name": "ClrSysMmbId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
        },
    )
    lei: Optional[str] = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress27Head00100104] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
        },
    )
    othr: Optional[GenericFinancialIdentification1Head00100104] = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
        },
    )


@dataclass
class Party52ChoiceHead00100104(ISO20022MessageElement):
    org_id: Optional[OrganisationIdentification39Head00100104] = field(
        default=None,
        metadata={
            "name": "OrgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
        },
    )
    prvt_id: Optional[PersonIdentification18Head00100104] = field(
        default=None,
        metadata={
            "name": "PrvtId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
        },
    )


@dataclass
class BranchAndFinancialInstitutionIdentification8Head00100104(ISO20022MessageElement):
    fin_instn_id: Optional[FinancialInstitutionIdentification23Head00100104] = field(
        default=None,
        metadata={
            "name": "FinInstnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "required": True,
        },
    )
    brnch_id: Optional[BranchData5Head00100104] = field(
        default=None,
        metadata={
            "name": "BrnchId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
        },
    )


@dataclass
class PartyIdentification272Head00100104(ISO20022MessageElement):
    nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "min_length": 1,
            "max_length": 140,
        },
    )
    pstl_adr: Optional[PostalAddress27Head00100104] = field(
        default=None,
        metadata={
            "name": "PstlAdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
        },
    )
    id: Optional[Party52ChoiceHead00100104] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
        },
    )
    ctry_of_res: Optional[str] = field(
        default=None,
        metadata={
            "name": "CtryOfRes",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    ctct_dtls: Optional[Contact13Head00100104] = field(
        default=None,
        metadata={
            "name": "CtctDtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
        },
    )


@dataclass
class Party51ChoiceHead00100104(ISO20022MessageElement):
    org_id: Optional[PartyIdentification272Head00100104] = field(
        default=None,
        metadata={
            "name": "OrgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
        },
    )
    fiid: Optional[BranchAndFinancialInstitutionIdentification8Head00100104] = field(
        default=None,
        metadata={
            "name": "FIId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
        },
    )


@dataclass
class BusinessApplicationHeader8Head00100104(ISO20022MessageElement):
    char_set: Optional[str] = field(
        default=None,
        metadata={
            "name": "CharSet",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
        },
    )
    fr: Optional[Party51ChoiceHead00100104] = field(
        default=None,
        metadata={
            "name": "Fr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "required": True,
        },
    )
    to: Optional[Party51ChoiceHead00100104] = field(
        default=None,
        metadata={
            "name": "To",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "required": True,
        },
    )
    biz_msg_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "BizMsgIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    msg_def_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgDefIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    biz_svc: Optional[str] = field(
        default=None,
        metadata={
            "name": "BizSvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mkt_prctc: Optional[ImplementationSpecification1Head00100104] = field(
        default=None,
        metadata={
            "name": "MktPrctc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
        },
    )
    cre_dt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "required": True,
        },
    )
    biz_prcg_dt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "BizPrcgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
        },
    )
    cpy_dplct: Optional[CopyDuplicate1Code] = field(
        default=None,
        metadata={
            "name": "CpyDplct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
        },
    )
    pssbl_dplct: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PssblDplct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
        },
    )
    prty: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
        },
    )
    sgntr: Optional[SignatureEnvelopeHead00100104] = field(
        default=None,
        metadata={
            "name": "Sgntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
        },
    )


@dataclass
class BusinessApplicationHeaderV04Head00100104(ISO20022MessageElement):
    char_set: Optional[str] = field(
        default=None,
        metadata={
            "name": "CharSet",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
        },
    )
    fr: Optional[Party51ChoiceHead00100104] = field(
        default=None,
        metadata={
            "name": "Fr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "required": True,
        },
    )
    to: Optional[Party51ChoiceHead00100104] = field(
        default=None,
        metadata={
            "name": "To",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "required": True,
        },
    )
    biz_msg_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "BizMsgIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    msg_def_idr: Optional[str] = field(
        default=None,
        metadata={
            "name": "MsgDefIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    biz_svc: Optional[str] = field(
        default=None,
        metadata={
            "name": "BizSvc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mkt_prctc: Optional[ImplementationSpecification1Head00100104] = field(
        default=None,
        metadata={
            "name": "MktPrctc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
        },
    )
    cre_dt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "required": True,
        },
    )
    biz_prcg_dt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "BizPrcgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
        },
    )
    cpy_dplct: Optional[CopyDuplicate1Code] = field(
        default=None,
        metadata={
            "name": "CpyDplct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
        },
    )
    pssbl_dplct: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PssblDplct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
        },
    )
    prty: Optional[str] = field(
        default=None,
        metadata={
            "name": "Prty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
        },
    )
    sgntr: Optional[SignatureEnvelopeHead00100104] = field(
        default=None,
        metadata={
            "name": "Sgntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
        },
    )
    rltd: list[BusinessApplicationHeader8Head00100104] = field(
        default_factory=list,
        metadata={
            "name": "Rltd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
        },
    )


@dataclass
class AppHdrHead00100104(BusinessApplicationHeaderV04, ISO20022MessageElement):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:head.001.001.04"
