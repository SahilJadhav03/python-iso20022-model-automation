from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from python_iso20022.base import ISO20022Message, ISO20022MessageElement
from python_iso20022.catp.enums import AtmserviceType5Code
from python_iso20022.enums import (
    Algorithm7Code,
    Algorithm8Code,
    Algorithm11Code,
    Algorithm12Code,
    Algorithm13Code,
    Algorithm15Code,
    AtmcustomerProfile1Code,
    AtmmediaType1Code,
    AtmmediaType4Code,
    AttributeType1Code,
    AuthenticationEntity2Code,
    AuthenticationMethod7Code,
    BytePadding1Code,
    CardDataReading1Code,
    CardDataReading4Code,
    CardholderVerificationCapability3Code,
    ContentType2Code,
    DataSetCategory7Code,
    EncryptionFormat1Code,
    MessageFunction11Code,
    OutputFormat1Code,
    PartyType12Code,
    Pinformat4Code,
    TransactionEnvironment2Code,
    TransactionEnvironment3Code,
    UserInterface5Code,
    Verification1Code,
)

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03"


@dataclass
class Acquirer7Catp01000103(ISO20022MessageElement):
    acqrg_instn: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcqrgInstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    brnch: Optional[str] = field(
        default=None,
        metadata={
            "name": "Brnch",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GeographicCoordinates1Catp01000103(ISO20022MessageElement):
    lat: Optional[str] = field(
        default=None,
        metadata={
            "name": "Lat",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 16,
        },
    )
    long: Optional[str] = field(
        default=None,
        metadata={
            "name": "Long",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 16,
        },
    )


@dataclass
class Kekidentifier2Catp01000103(ISO20022MessageElement):
    class Meta:
        name = "KEKIdentifier2"

    key_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    key_vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )
    seq_nb: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "SeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    derivtn_id: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "DerivtnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "min_length": 5,
            "max_length": 16,
            "format": "base64",
        },
    )


@dataclass
class PlainCardData25Catp01000103(ISO20022MessageElement):
    pan: Optional[str] = field(
        default=None,
        metadata={
            "name": "PAN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "pattern": r"[0-9]{8,28}",
        },
    )
    card_seq_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "CardSeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "pattern": r"[0-9]{2,3}",
        },
    )
    fctv_dt: Optional[str] = field(
        default=None,
        metadata={
            "name": "FctvDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "min_length": 1,
            "max_length": 10,
        },
    )
    xpry_dt: Optional[str] = field(
        default=None,
        metadata={
            "name": "XpryDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "pattern": r"([0-9]{4,4}-[0-9]{2,2}-[0-9]{2,2})|([0-9]{2,2}-[0-9]{2,2})|([0-9]{4,4}-[0-9]{2,2})",
        },
    )
    svc_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "SvcCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "pattern": r"[0-9]{3}",
        },
    )
    trck1: Optional[str] = field(
        default=None,
        metadata={
            "name": "Trck1",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "min_length": 1,
            "max_length": 76,
        },
    )
    trck2: Optional[str] = field(
        default=None,
        metadata={
            "name": "Trck2",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "min_length": 1,
            "max_length": 37,
        },
    )
    trck3: Optional[str] = field(
        default=None,
        metadata={
            "name": "Trck3",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "min_length": 1,
            "max_length": 104,
        },
    )
    crdhldr_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "CrdhldrNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "min_length": 1,
            "max_length": 45,
        },
    )


@dataclass
class TransactionIdentifier3Catp01000103(ISO20022MessageElement):
    tx_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TxDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "required": True,
        },
    )
    hst_tx_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "HstTxDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
        },
    )
    tx_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "TxRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Utmcoordinates1Catp01000103(ISO20022MessageElement):
    class Meta:
        name = "UTMCoordinates1"

    utmzone: Optional[str] = field(
        default=None,
        metadata={
            "name": "UTMZone",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 16,
        },
    )
    utmestwrd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "UTMEstwrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    utmnrthwrd: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "UTMNrthwrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "required": True,
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )


@dataclass
class AtmconfigurationParameter1Catp01000103(ISO20022MessageElement):
    class Meta:
        name = "ATMConfigurationParameter1"

    tp: Optional[DataSetCategory7Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "required": True,
        },
    )
    vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AtmcustomerProfile6Catp01000103(ISO20022MessageElement):
    class Meta:
        name = "ATMCustomerProfile6"

    rtrvl_md: Optional[AtmcustomerProfile1Code] = field(
        default=None,
        metadata={
            "name": "RtrvlMd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "required": True,
        },
    )
    prfl_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrflRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cstmr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CstmrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prefrd_lang: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrefrdLang",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
        },
    )


@dataclass
class AtmmessageFunction2Catp01000103(ISO20022MessageElement):
    class Meta:
        name = "ATMMessageFunction2"

    fctn: Optional[MessageFunction11Code] = field(
        default=None,
        metadata={
            "name": "Fctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "required": True,
        },
    )
    atmsvc_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "ATMSvcCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    hst_svc_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "HstSvcCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class Atmservice20Catp01000103(ISO20022MessageElement):
    class Meta:
        name = "ATMService20"

    svc_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "SvcRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    atmsvc_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "ATMSvcCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    svc_tp: Optional[AtmserviceType5Code] = field(
        default=None,
        metadata={
            "name": "SvcTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "required": True,
        },
    )
    svc_varnt_id: list[str] = field(
        default_factory=list,
        metadata={
            "name": "SvcVarntId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DisplayCapabilities5Catp01000103(ISO20022MessageElement):
    dstn: list[UserInterface5Code] = field(
        default_factory=list,
        metadata={
            "name": "Dstn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "min_occurs": 1,
        },
    )
    avlbl_frmt: list[OutputFormat1Code] = field(
        default_factory=list,
        metadata={
            "name": "AvlblFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
        },
    )
    nb_of_lines: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NbOfLines",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    line_width: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "LineWidth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    avlbl_lang: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AvlblLang",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
        },
    )


@dataclass
class EncapsulatedContent3Catp01000103(ISO20022MessageElement):
    cntt_tp: Optional[ContentType2Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "required": True,
        },
    )
    cntt: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Cntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "min_length": 1,
            "max_length": 102400,
            "format": "base64",
        },
    )


@dataclass
class GenericIdentification77Catp01000103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    tp: Optional[PartyType12Code] = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "required": True,
        },
    )
    issr: Optional[PartyType12Code] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "pattern": r"[a-zA-Z]{2,3}",
        },
    )
    shrt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class GeographicLocation1ChoiceCatp01000103(ISO20022MessageElement):
    geogc_cordints: Optional[GeographicCoordinates1Catp01000103] = field(
        default=None,
        metadata={
            "name": "GeogcCordints",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
        },
    )
    utmcordints: Optional[Utmcoordinates1Catp01000103] = field(
        default=None,
        metadata={
            "name": "UTMCordints",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
        },
    )


@dataclass
class Parameter5Catp01000103(ISO20022MessageElement):
    dgst_algo: Optional[Algorithm11Code] = field(
        default=None,
        metadata={
            "name": "DgstAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
        },
    )


@dataclass
class Parameter6Catp01000103(ISO20022MessageElement):
    ncrptn_frmt: Optional[EncryptionFormat1Code] = field(
        default=None,
        metadata={
            "name": "NcrptnFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
        },
    )
    initlstn_vctr: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "InitlstnVctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "min_length": 1,
            "max_length": 500,
            "format": "base64",
        },
    )
    bpddg: Optional[BytePadding1Code] = field(
        default=None,
        metadata={
            "name": "BPddg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
        },
    )


@dataclass
class Parameter7Catp01000103(ISO20022MessageElement):
    initlstn_vctr: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "InitlstnVctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "min_length": 1,
            "max_length": 500,
            "format": "base64",
        },
    )
    bpddg: Optional[BytePadding1Code] = field(
        default=None,
        metadata={
            "name": "BPddg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
        },
    )


@dataclass
class RelativeDistinguishedName1Catp01000103(ISO20022MessageElement):
    attr_tp: Optional[AttributeType1Code] = field(
        default=None,
        metadata={
            "name": "AttrTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "required": True,
        },
    )
    attr_val: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttrVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 140,
        },
    )


@dataclass
class TerminalHosting1Catp01000103(ISO20022MessageElement):
    ctgy: Optional[TransactionEnvironment3Code] = field(
        default=None,
        metadata={
            "name": "Ctgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class TransactionVerificationResult5Catp01000103(ISO20022MessageElement):
    mtd: Optional[AuthenticationMethod7Code] = field(
        default=None,
        metadata={
            "name": "Mtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "required": True,
        },
    )
    vrfctn_ntty: Optional[AuthenticationEntity2Code] = field(
        default=None,
        metadata={
            "name": "VrfctnNtty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
        },
    )
    rslt: Optional[Verification1Code] = field(
        default=None,
        metadata={
            "name": "Rslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
        },
    )
    addtl_rslt: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlRslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "min_length": 1,
            "max_length": 500,
        },
    )
    authntcn_tkn: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "AuthntcnTkn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "min_length": 1,
            "max_length": 140,
            "format": "base64",
        },
    )


@dataclass
class Atmcontext16Catp01000103(ISO20022MessageElement):
    class Meta:
        name = "ATMContext16"

    ssn_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "SsnRef",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    svc: Optional[Atmservice20Catp01000103] = field(
        default=None,
        metadata={
            "name": "Svc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "required": True,
        },
    )


@dataclass
class Atmequipment1Catp01000103(ISO20022MessageElement):
    class Meta:
        name = "ATMEquipment1"

    manfctr: Optional[str] = field(
        default=None,
        metadata={
            "name": "Manfctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    mdl: Optional[str] = field(
        default=None,
        metadata={
            "name": "Mdl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    srl_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "SrlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    appl_prvdr: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApplPrvdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    appl_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApplNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    appl_vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApplVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    apprvl_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApprvlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    cfgtn_param: list[AtmconfigurationParameter1Catp01000103] = field(
        default_factory=list,
        metadata={
            "name": "CfgtnParam",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
        },
    )


@dataclass
class AlgorithmIdentification12Catp01000103(ISO20022MessageElement):
    algo: Optional[Algorithm8Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "required": True,
        },
    )
    param: Optional[Parameter5Catp01000103] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
        },
    )


@dataclass
class AlgorithmIdentification13Catp01000103(ISO20022MessageElement):
    algo: Optional[Algorithm13Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "required": True,
        },
    )
    param: Optional[Parameter6Catp01000103] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
        },
    )


@dataclass
class AlgorithmIdentification14Catp01000103(ISO20022MessageElement):
    algo: Optional[Algorithm15Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "required": True,
        },
    )
    param: Optional[Parameter6Catp01000103] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
        },
    )


@dataclass
class AlgorithmIdentification15Catp01000103(ISO20022MessageElement):
    algo: Optional[Algorithm12Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "required": True,
        },
    )
    param: Optional[Parameter7Catp01000103] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
        },
    )


@dataclass
class CertificateIssuer1Catp01000103(ISO20022MessageElement):
    rltv_dstngshd_nm: list[RelativeDistinguishedName1Catp01000103] = field(
        default_factory=list,
        metadata={
            "name": "RltvDstngshdNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "min_occurs": 1,
        },
    )


@dataclass
class PointOfInteractionCapabilities10Catp01000103(ISO20022MessageElement):
    card_rd_data: list[CardDataReading4Code] = field(
        default_factory=list,
        metadata={
            "name": "CardRdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
        },
    )
    card_wrt_data: list[CardDataReading4Code] = field(
        default_factory=list,
        metadata={
            "name": "CardWrtData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
        },
    )
    authntcn: list[CardholderVerificationCapability3Code] = field(
        default_factory=list,
        metadata={
            "name": "Authntcn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
        },
    )
    pinlngth_cpblties: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PINLngthCpblties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    apprvl_cd_lngth: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ApprvlCdLngth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    mx_scrpt_lngth: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MxScrptLngth",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    card_captr_cpbl: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CardCaptrCpbl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
        },
    )
    wdrwl_mdia: list[AtmmediaType1Code] = field(
        default_factory=list,
        metadata={
            "name": "WdrwlMdia",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
        },
    )
    dpstd_mdia: list[AtmmediaType4Code] = field(
        default_factory=list,
        metadata={
            "name": "DpstdMdia",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
        },
    )
    msg_cpblties: list[DisplayCapabilities5Catp01000103] = field(
        default_factory=list,
        metadata={
            "name": "MsgCpblties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
        },
    )
    intractv_txs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "IntractvTxs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "min_length": 1,
            "max_length": 256,
        },
    )
    rct_prtg: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RctPrtg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
        },
    )


@dataclass
class PostalAddress17Catp01000103(ISO20022MessageElement):
    adr_line: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AdrLine",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "max_occurs": 2,
            "min_length": 1,
            "max_length": 70,
        },
    )
    strt_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrtNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "min_length": 1,
            "max_length": 70,
        },
    )
    bldg_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "BldgNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "min_length": 1,
            "max_length": 16,
        },
    )
    pst_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "PstCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "min_length": 1,
            "max_length": 16,
        },
    )
    twn_nm: Optional[str] = field(
        default=None,
        metadata={
            "name": "TwnNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry_sub_dvsn: list[str] = field(
        default_factory=list,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "max_occurs": 2,
            "min_length": 1,
            "max_length": 35,
        },
    )
    ctry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "required": True,
            "pattern": r"[A-Z]{2,2}",
        },
    )
    glctn: Optional[GeographicLocation1ChoiceCatp01000103] = field(
        default=None,
        metadata={
            "name": "GLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
        },
    )


@dataclass
class Traceability4Catp01000103(ISO20022MessageElement):
    rlay_id: Optional[GenericIdentification77Catp01000103] = field(
        default=None,
        metadata={
            "name": "RlayId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "required": True,
        },
    )
    seq_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "SeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    trac_dt_tm_in: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TracDtTmIn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "required": True,
        },
    )
    trac_dt_tm_out: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TracDtTmOut",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "required": True,
        },
    )


@dataclass
class AutomatedTellerMachine12Catp01000103(ISO20022MessageElement):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    addtl_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    seq_nb: Optional[str] = field(
        default=None,
        metadata={
            "name": "SeqNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    base_ccy: Optional[str] = field(
        default=None,
        metadata={
            "name": "BaseCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "required": True,
            "pattern": r"[A-Z]{3,3}",
        },
    )
    lctn: Optional[PostalAddress17Catp01000103] = field(
        default=None,
        metadata={
            "name": "Lctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
        },
    )
    lctn_ctgy: Optional[TransactionEnvironment2Code] = field(
        default=None,
        metadata={
            "name": "LctnCtgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
        },
    )
    cpblties: Optional[PointOfInteractionCapabilities10Catp01000103] = field(
        default=None,
        metadata={
            "name": "Cpblties",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
        },
    )
    eqpmnt: Optional[Atmequipment1Catp01000103] = field(
        default=None,
        metadata={
            "name": "Eqpmnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
        },
    )


@dataclass
class EncryptedContent3Catp01000103(ISO20022MessageElement):
    cntt_tp: Optional[ContentType2Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "required": True,
        },
    )
    cntt_ncrptn_algo: Optional[AlgorithmIdentification14Catp01000103] = field(
        default=None,
        metadata={
            "name": "CnttNcrptnAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "required": True,
        },
    )
    ncrptd_data: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "NcrptdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 102400,
            "format": "base64",
        },
    )


@dataclass
class Header31Catp01000103(ISO20022MessageElement):
    msg_fctn: Optional[AtmmessageFunction2Catp01000103] = field(
        default=None,
        metadata={
            "name": "MsgFctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "required": True,
        },
    )
    prtcol_vrsn: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrtcolVrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 6,
        },
    )
    xchg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "XchgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "required": True,
            "pattern": r"[0-9]{1,3}",
        },
    )
    cre_dt_tm: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "required": True,
        },
    )
    initg_pty: Optional[str] = field(
        default=None,
        metadata={
            "name": "InitgPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    rcpt_pty: Optional[str] = field(
        default=None,
        metadata={
            "name": "RcptPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    prc_stat: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrcStat",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    tracblt: list[Traceability4Catp01000103] = field(
        default_factory=list,
        metadata={
            "name": "Tracblt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
        },
    )


@dataclass
class IssuerAndSerialNumber1Catp01000103(ISO20022MessageElement):
    issr: Optional[CertificateIssuer1Catp01000103] = field(
        default=None,
        metadata={
            "name": "Issr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "required": True,
        },
    )
    srl_nb: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "SrlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 35,
            "format": "base64",
        },
    )


@dataclass
class Kek4Catp01000103(ISO20022MessageElement):
    class Meta:
        name = "KEK4"

    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    kekid: Optional[Kekidentifier2Catp01000103] = field(
        default=None,
        metadata={
            "name": "KEKId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "required": True,
        },
    )
    key_ncrptn_algo: Optional[AlgorithmIdentification13Catp01000103] = field(
        default=None,
        metadata={
            "name": "KeyNcrptnAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "required": True,
        },
    )
    ncrptd_key: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "NcrptdKey",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 500,
            "format": "base64",
        },
    )


@dataclass
class Parameter4Catp01000103(ISO20022MessageElement):
    ncrptn_frmt: Optional[EncryptionFormat1Code] = field(
        default=None,
        metadata={
            "name": "NcrptnFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
        },
    )
    dgst_algo: Optional[Algorithm11Code] = field(
        default=None,
        metadata={
            "name": "DgstAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
        },
    )
    msk_gnrtr_algo: Optional[AlgorithmIdentification12Catp01000103] = field(
        default=None,
        metadata={
            "name": "MskGnrtrAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
        },
    )


@dataclass
class AlgorithmIdentification11Catp01000103(ISO20022MessageElement):
    algo: Optional[Algorithm7Code] = field(
        default=None,
        metadata={
            "name": "Algo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "required": True,
        },
    )
    param: Optional[Parameter4Catp01000103] = field(
        default=None,
        metadata={
            "name": "Param",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
        },
    )


@dataclass
class Recipient5ChoiceCatp01000103(ISO20022MessageElement):
    issr_and_srl_nb: Optional[IssuerAndSerialNumber1Catp01000103] = field(
        default=None,
        metadata={
            "name": "IssrAndSrlNb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
        },
    )
    key_idr: Optional[Kekidentifier2Catp01000103] = field(
        default=None,
        metadata={
            "name": "KeyIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
        },
    )


@dataclass
class KeyTransport4Catp01000103(ISO20022MessageElement):
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rcpt_id: Optional[Recipient5ChoiceCatp01000103] = field(
        default=None,
        metadata={
            "name": "RcptId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "required": True,
        },
    )
    key_ncrptn_algo: Optional[AlgorithmIdentification11Catp01000103] = field(
        default=None,
        metadata={
            "name": "KeyNcrptnAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "required": True,
        },
    )
    ncrptd_key: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "NcrptdKey",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 5000,
            "format": "base64",
        },
    )


@dataclass
class Recipient4ChoiceCatp01000103(ISO20022MessageElement):
    key_trnsprt: Optional[KeyTransport4Catp01000103] = field(
        default=None,
        metadata={
            "name": "KeyTrnsprt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
        },
    )
    kek: Optional[Kek4Catp01000103] = field(
        default=None,
        metadata={
            "name": "KEK",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
        },
    )
    key_idr: Optional[Kekidentifier2Catp01000103] = field(
        default=None,
        metadata={
            "name": "KeyIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
        },
    )


@dataclass
class AuthenticatedData4Catp01000103(ISO20022MessageElement):
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rcpt: list[Recipient4ChoiceCatp01000103] = field(
        default_factory=list,
        metadata={
            "name": "Rcpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "min_occurs": 1,
        },
    )
    macalgo: Optional[AlgorithmIdentification15Catp01000103] = field(
        default=None,
        metadata={
            "name": "MACAlgo",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "required": True,
        },
    )
    ncpsltd_cntt: Optional[EncapsulatedContent3Catp01000103] = field(
        default=None,
        metadata={
            "name": "NcpsltdCntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "required": True,
        },
    )
    mac: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "MAC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "required": True,
            "min_length": 1,
            "max_length": 140,
            "format": "base64",
        },
    )


@dataclass
class EnvelopedData4Catp01000103(ISO20022MessageElement):
    vrsn: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "total_digits": 18,
            "fraction_digits": 0,
        },
    )
    rcpt: list[Recipient4ChoiceCatp01000103] = field(
        default_factory=list,
        metadata={
            "name": "Rcpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "min_occurs": 1,
        },
    )
    ncrptd_cntt: Optional[EncryptedContent3Catp01000103] = field(
        default=None,
        metadata={
            "name": "NcrptdCntt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
        },
    )


@dataclass
class ContentInformationType10Catp01000103(ISO20022MessageElement):
    cntt_tp: Optional[ContentType2Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "required": True,
        },
    )
    envlpd_data: Optional[EnvelopedData4Catp01000103] = field(
        default=None,
        metadata={
            "name": "EnvlpdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "required": True,
        },
    )


@dataclass
class ContentInformationType15Catp01000103(ISO20022MessageElement):
    cntt_tp: Optional[ContentType2Code] = field(
        default=None,
        metadata={
            "name": "CnttTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "required": True,
        },
    )
    authntcd_data: Optional[AuthenticatedData4Catp01000103] = field(
        default=None,
        metadata={
            "name": "AuthntcdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "required": True,
        },
    )


@dataclass
class OnLinePin5Catp01000103(ISO20022MessageElement):
    class Meta:
        name = "OnLinePIN5"

    ncrptd_pinblck: Optional[ContentInformationType10Catp01000103] = field(
        default=None,
        metadata={
            "name": "NcrptdPINBlck",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "required": True,
        },
    )
    pinfrmt: Optional[Pinformat4Code] = field(
        default=None,
        metadata={
            "name": "PINFrmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "required": True,
        },
    )
    addtl_inpt: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddtlInpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class PaymentCard36Catp01000103(ISO20022MessageElement):
    card_data_ntry_md: Optional[CardDataReading1Code] = field(
        default=None,
        metadata={
            "name": "CardDataNtryMd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "required": True,
        },
    )
    fllbck_ind: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FllbckInd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
        },
    )
    prtctd_card_data: Optional[ContentInformationType10Catp01000103] = field(
        default=None,
        metadata={
            "name": "PrtctdCardData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
        },
    )
    plain_card_data: Optional[PlainCardData25Catp01000103] = field(
        default=None,
        metadata={
            "name": "PlainCardData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
        },
    )
    card_ctry_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "CardCtryCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "min_length": 1,
            "max_length": 3,
        },
    )
    card_ccy_cd: Optional[str] = field(
        default=None,
        metadata={
            "name": "CardCcyCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "pattern": r"[a-zA-Z0-9]{3}",
        },
    )


@dataclass
class Atmtransaction43Catp01000103(ISO20022MessageElement):
    class Meta:
        name = "ATMTransaction43"

    tx_id: Optional[TransactionIdentifier3Catp01000103] = field(
        default=None,
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "required": True,
        },
    )
    rcncltn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RcncltnId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    crdhldr_new_pin: Optional[OnLinePin5Catp01000103] = field(
        default=None,
        metadata={
            "name": "CrdhldrNewPIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
        },
    )
    iccrltd_data: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "ICCRltdData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "min_length": 1,
            "max_length": 10000,
            "format": "base64",
        },
    )


@dataclass
class CardholderAuthentication8Catp01000103(ISO20022MessageElement):
    authntcn_mtd: Optional[AuthenticationMethod7Code] = field(
        default=None,
        metadata={
            "name": "AuthntcnMtd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "required": True,
        },
    )
    tkn_reqd: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TknReqd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
        },
    )
    authntcn_val: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "AuthntcnVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "min_length": 1,
            "max_length": 5000,
            "format": "base64",
        },
    )
    prtctd_authntcn_val: Optional[ContentInformationType10Catp01000103] = field(
        default=None,
        metadata={
            "name": "PrtctdAuthntcnVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
        },
    )
    crdhldr_on_line_pin: Optional[OnLinePin5Catp01000103] = field(
        default=None,
        metadata={
            "name": "CrdhldrOnLinePIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
        },
    )


@dataclass
class Atmcustomer8Catp01000103(ISO20022MessageElement):
    class Meta:
        name = "ATMCustomer8"

    prfl: Optional[AtmcustomerProfile6Catp01000103] = field(
        default=None,
        metadata={
            "name": "Prfl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
        },
    )
    selctd_lang: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelctdLang",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
        },
    )
    authntcn: list[CardholderAuthentication8Catp01000103] = field(
        default_factory=list,
        metadata={
            "name": "Authntcn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "min_occurs": 1,
        },
    )
    authntcn_rslt: list[TransactionVerificationResult5Catp01000103] = field(
        default_factory=list,
        metadata={
            "name": "AuthntcnRslt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
        },
    )


@dataclass
class Atmenvironment18Catp01000103(ISO20022MessageElement):
    class Meta:
        name = "ATMEnvironment18"

    acqrr: Optional[Acquirer7Catp01000103] = field(
        default=None,
        metadata={
            "name": "Acqrr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
        },
    )
    atmmgr_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ATMMgrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "min_length": 1,
            "max_length": 35,
        },
    )
    hstg_ntty: Optional[TerminalHosting1Catp01000103] = field(
        default=None,
        metadata={
            "name": "HstgNtty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
        },
    )
    atm: Optional[AutomatedTellerMachine12Catp01000103] = field(
        default=None,
        metadata={
            "name": "ATM",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "required": True,
        },
    )
    cstmr: Optional[Atmcustomer8Catp01000103] = field(
        default=None,
        metadata={
            "name": "Cstmr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "required": True,
        },
    )
    card: Optional[PaymentCard36Catp01000103] = field(
        default=None,
        metadata={
            "name": "Card",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
        },
    )


@dataclass
class AtmpinmanagementRequest3Catp01000103(ISO20022MessageElement):
    class Meta:
        name = "ATMPINManagementRequest3"

    envt: Optional[Atmenvironment18Catp01000103] = field(
        default=None,
        metadata={
            "name": "Envt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "required": True,
        },
    )
    cntxt: Optional[Atmcontext16Catp01000103] = field(
        default=None,
        metadata={
            "name": "Cntxt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "required": True,
        },
    )
    tx: Optional[Atmtransaction43Catp01000103] = field(
        default=None,
        metadata={
            "name": "Tx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "required": True,
        },
    )


@dataclass
class AtmpinmanagementRequestV03Catp01000103(ISO20022MessageElement):
    class Meta:
        name = "ATMPINManagementRequestV03"

    hdr: Optional[Header31Catp01000103] = field(
        default=None,
        metadata={
            "name": "Hdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
            "required": True,
        },
    )
    prtctd_atmpinmgmt_req: Optional[ContentInformationType10Catp01000103] = field(
        default=None,
        metadata={
            "name": "PrtctdATMPINMgmtReq",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
        },
    )
    atmpinmgmt_req: Optional[AtmpinmanagementRequest3Catp01000103] = field(
        default=None,
        metadata={
            "name": "ATMPINMgmtReq",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
        },
    )
    scty_trlr: Optional[ContentInformationType15Catp01000103] = field(
        default=None,
        metadata={
            "name": "SctyTrlr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
        },
    )


@dataclass
class Catp01000103(ISO20022Message):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03"

    atmpinmgmt_req: Optional[AtmpinmanagementRequestV03Catp01000103] = field(
        default=None,
        metadata={
            "name": "ATMPINMgmtReq",
            "type": "Element",
            "required": True,
        },
    )
