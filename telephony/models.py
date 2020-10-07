# coding: utf-8
from sqlalchemy import CHAR, Column, DateTime, Enum, Float, Index, String, TIMESTAMP, text
from sqlalchemy.dialects.mysql import BIGINT, INTEGER, MEDIUMBLOB, MEDIUMTEXT, SMALLINT, TINYINT
# from sqlalchemy.orm import relationship

from database import Base

metadata = Base.metadata


class CdrOut(Base):
    __tablename__ = 'cdr_out'

    id = Column(INTEGER(11), primary_key=True)
    amaflags = Column(String(50))
    src = Column(String(80), nullable=False, index=True, server_default=text("''"))
    dst = Column(String(80), nullable=False, index=True, server_default=text("''"))
    calltype = Column(SMALLINT(6), nullable=False)
    minute_rate = Column(Float, nullable=False)
    billsec = Column(INTEGER(11))
    cost = Column(Float, nullable=False)
    start = Column(DateTime, index=True)
    end = Column(DateTime)
    duration = Column(INTEGER(11))
    disposition = Column(Enum('ANSWERED', 'BUSY', 'FAILED', 'NO ANSWER', 'CONGESTION'))
    answer = Column(DateTime)
    clid = Column(String(80), nullable=False, index=True, server_default=text("''"))
    dcontext = Column(String(80), nullable=False, index=True, server_default=text("''"))
    channel = Column(String(50))
    dstchannel = Column(String(50))
    uniqueid = Column(String(32), nullable=False, server_default=text("''"))
    userfield = Column(String(255))


class CdrSvi(Base):
    __tablename__ = 'cdr_svi'

    id = Column(INTEGER(11), primary_key=True)
    line_in = Column(String(64), nullable=False)
    ref = Column(String(80), nullable=False)
    ref_id = Column(INTEGER(11), nullable=False)
    contact_id = Column(INTEGER(11), nullable=False)
    num_compose = Column(String(20), nullable=False)
    src = Column(String(80), nullable=False, index=True, server_default=text("''"))
    dst = Column(String(80), nullable=False, index=True, server_default=text("''"))
    duration = Column(INTEGER(11))
    billsec = Column(INTEGER(11))
    start = Column(DateTime, index=True)
    answer = Column(DateTime)
    end = Column(DateTime)
    calltype = Column(SMALLINT(6), nullable=False)
    disposition = Column(Enum('ANSWERED', 'BUSY', 'FAILED', 'NO ANSWER', 'CONGESTION'))
    clid = Column(String(80), nullable=False, index=True, server_default=text("''"))
    dcontext = Column(String(80), nullable=False, index=True, server_default=text("''"))
    channel = Column(String(50))
    dstchannel = Column(String(50))
    uniqueid = Column(String(32), nullable=False, server_default=text("''"))
    userfield = Column(String(255))
    amaflags = Column(String(50))


class Followme(Base):
    __tablename__ = 'followmes'

    name = Column(INTEGER(11), primary_key=True)
    ref = Column(String(32), nullable=False)
    ref_id = Column(INTEGER(11), nullable=False)
    label = Column(String(64), nullable=False)
    context = Column(String(64), nullable=False, server_default=text("'appelPortable'"))
    musiconhold = Column(String(64))
    takecall = Column(CHAR(1))
    declinecall = Column(CHAR(1))
    call_from_record = Column(TINYINT(1), nullable=False, server_default=text("'1'"))
    call_from_prompt = Column(String(64))
    norecording_prompt = Column(String(64))
    options_prompt = Column(String(64))
    hold_prompt = Column(String(64))
    status_prompt = Column(String(64))
    sorry_prompt = Column(String(64))
    commented = Column(TINYINT(1), nullable=False)
    transfert_type = Column(INTEGER(11), nullable=False)


class Followmesnumber(Base):
    __tablename__ = 'followmesnumbers'

    id = Column(INTEGER(11), primary_key=True)
    name = Column(INTEGER(11), nullable=False)
    label = Column(String(128), nullable=False)
    ordinal = Column(INTEGER(11), nullable=False, server_default=text("'1'"))
    phonenumber = Column(String(255), nullable=False)
    timeout = Column(INTEGER(11), nullable=False)
    commented = Column(TINYINT(1), server_default=text("'0'"))


class Number(Base):
    __tablename__ = 'numbers'

    id = Column(INTEGER(11), primary_key=True)
    num = Column(String(45), comment='Numéro externe à diriger sur un compte sip medbox')
    sipfriends_id = Column(INTEGER(11))


class Rappel(Base):
    __tablename__ = 'rappels'

    id = Column(INTEGER(8), primary_key=True)
    phone = Column(String(64))
    datetime = Column(TIMESTAMP, nullable=False, index=True, server_default=text("'0000-00-00 00:00:00'"))
    attempts = Column(INTEGER(8), server_default=text("'0'"))
    pickups = Column(INTEGER(8), server_default=text("'0'"))
    disposition = Column(INTEGER(8), server_default=text("'0'"))
    reason = Column(String(255), server_default=text("'Unknow'"))
    duration = Column(INTEGER(8), server_default=text("'0'"))
    param = Column(String(255), server_default=text("''"))
    result = Column(String(255), server_default=text("''"))
    cause = Column(String(255), server_default=text("''"))
    lastupdated = Column(TIMESTAMP, nullable=False, index=True, server_default=text("'0000-00-00 00:00:00'"))


class Sipfriend(Base):
    __tablename__ = 'sipfriends'
    __table_args__ = (
        Index('ipaddr', 'ipaddr', 'port'),
        Index('host', 'host', 'port')
    )

    id = Column(INTEGER(11), primary_key=True)
    type = Column(Enum('friend', 'user', 'peer'))
    name = Column(String(128), nullable=False, unique=True)
    secret = Column(String(128))
    context = Column(String(128))
    host = Column(String(64))
    defaultuser = Column(String(128))
    ipaddr = Column(String(45))
    port = Column(INTEGER(5))
    regseconds = Column(INTEGER(11))
    fullcontact = Column(String(128))
    regserver = Column(String(64))
    useragent = Column(String(64))
    lastms = Column(INTEGER(11))
    mailbox = Column(String(128))
    remotesecret = Column(String(128))
    accountcode = Column(String(40))
    useclientcode = Column(Enum('yes', 'no'))
    callerid = Column(String(128))
    deny = Column(String(40))
    permit = Column(String(40))
    md5secret = Column(String(128))
    transport = Column(Enum('udp', 'tcp', 'udp,tcp', 'tcp,udp', 'tls'))
    dtmfmode = Column(Enum('rfc2833', 'info', 'shortinfo', 'inband', 'auto'))
    directmedia = Column(Enum('yes', 'no', 'nonat', 'update'))
    nat = Column(Enum('yes', 'no', 'never', 'route'))
    callgroup = Column(String(40))
    pickupgroup = Column(String(40))
    language = Column(String(40))
    disallow = Column(String(40))
    allow = Column(String(40))
    insecure = Column(String(40))
    trustrpid = Column(Enum('yes', 'no'))
    progressinband = Column(Enum('yes', 'no', 'never'))
    promiscredir = Column(Enum('yes', 'no'))
    setvar = Column(String(40))
    amaflags = Column(String(40))
    callcounter = Column(Enum('yes', 'no'))
    busylevel = Column(INTEGER(11))
    allowoverlap = Column(Enum('yes', 'no'))
    allowsubscribe = Column(Enum('yes', 'no'))
    videosupport = Column(Enum('yes', 'no'))
    maxcallbitrate = Column(INTEGER(11))
    rfc2833compensate = Column(Enum('yes', 'no'))
    session_timers = Column('session-timers', Enum('accept', 'refuse', 'originate'))
    session_expires = Column('session-expires', INTEGER(11))
    session_minse = Column('session-minse', INTEGER(11))
    session_refresher = Column('session-refresher', Enum('uac', 'uas'))
    t38pt_usertpsource = Column(String(128))
    regexten = Column(String(128))
    fromdomain = Column(String(128))
    fromuser = Column(String(128))
    qualify = Column(String(40))
    defaultip = Column(String(40))
    rtptimeout = Column(INTEGER(11))
    rtpholdtimeout = Column(INTEGER(11))
    sendrpid = Column(Enum('yes', 'no'))
    outboundproxy = Column(String(128))
    callbackextension = Column(String(128))
    registertrying = Column(Enum('yes', 'no'))
    timert1 = Column(INTEGER(11))
    timerb = Column(INTEGER(11))
    qualifyfreq = Column(INTEGER(11))
    constantssrc = Column(Enum('yes', 'no'))
    contactpermit = Column(String(40))
    contactdeny = Column(String(40))
    usereqphone = Column(Enum('yes', 'no'))
    textsupport = Column(Enum('yes', 'no'))
    faxdetect = Column(Enum('yes', 'no'))
    buggymwi = Column(Enum('yes', 'no'))
    auth = Column(String(128))
    fullname = Column(String(128))
    trunkname = Column(String(128))
    cid_number = Column(String(64))
    callingpres = Column(Enum('allowed_not_screened', 'allowed_passed_screen', 'allowed_failed_screen', 'allowed', 'prohib_not_screened', 'prohib_passed_screen', 'prohib_failed_screen', 'prohib'))
    mohinterpret = Column(String(40))
    mohsuggest = Column(String(40))
    parkinglot = Column(String(40))
    hasvoicemail = Column(Enum('yes', 'no'))
    subscribemwi = Column(Enum('yes', 'no'))
    vmexten = Column(String(64))
    autoframing = Column(Enum('yes', 'no'))
    rtpkeepalive = Column(INTEGER(11))
    call_limit = Column('call-limit', INTEGER(11))
    g726nonstandard = Column(Enum('yes', 'no'))
    ignoresdpversion = Column(Enum('yes', 'no'))
    allowtransfer = Column(Enum('yes', 'no'))
    dynamic = Column(Enum('yes', 'no'))


class VoicemailMessage(Base):
    __tablename__ = 'voicemail_messages'
    __table_args__ = (
        Index('index', 'mailboxuser', 'mailboxcontext', 'read'),
    )

    id = Column(BIGINT(20), primary_key=True, unique=True)
    msgnum = Column(INTEGER(4), nullable=False)
    dir = Column(String(128), nullable=False, index=True)
    context = Column(String(80), nullable=False)
    macrocontext = Column(String(80))
    callerid = Column(String(40), nullable=False)
    origtime = Column(String(40), nullable=False)
    duration = Column(String(20), nullable=False)
    mailboxuser = Column(INTEGER(11), nullable=False)
    mailboxcontext = Column(String(80), nullable=False)
    recording = Column(MEDIUMBLOB, nullable=False)
    content = Column(MEDIUMTEXT)
    label = Column(String(30), nullable=False)
    read = Column(TINYINT(1), nullable=False)
    answered = Column(TINYINT(1), nullable=False)
    flag = Column(String(10), nullable=False)
    deleted = Column(TINYINT(1), nullable=False)
    voicemail_messagescol = Column(String(45))
    msg_id = Column(String(40))


class VoicemailUser(Base):
    __tablename__ = 'voicemail_users'
    __table_args__ = (
        Index('mailbox_context', 'mailbox', 'context'),
    )

    id = Column(INTEGER(11), primary_key=True)
    uniqueid = Column(INTEGER(11), nullable=False)
    customer_id = Column(String(10))
    context = Column(String(10), nullable=False)
    mailbox = Column(String(10), nullable=False)
    password = Column(String(10), nullable=False)
    fullname = Column(String(150))
    email = Column(String(50))
    pager = Column(String(50))
    tz = Column(String(10), server_default=text("'central'"))
    attach = Column(Enum('yes', 'no'), nullable=False, server_default=text("'yes'"))
    saycid = Column(Enum('yes', 'no'), nullable=False, server_default=text("'yes'"))
    dialout = Column(String(10))
    callback = Column(String(10))
    review = Column(Enum('yes', 'no'), nullable=False, server_default=text("'no'"))
    operator = Column(Enum('yes', 'no'), nullable=False, server_default=text("'no'"))
    envelope = Column(Enum('yes', 'no'), nullable=False, server_default=text("'no'"))
    sayduration = Column(Enum('yes', 'no'), nullable=False, server_default=text("'no'"))
    saydurationm = Column(TINYINT(4), nullable=False, server_default=text("'1'"))
    sendvoicemail = Column(Enum('yes', 'no'), nullable=False, server_default=text("'no'"))
    delete = Column(Enum('yes', 'no'), nullable=False, server_default=text("'no'"))
    nextaftercmd = Column(Enum('yes', 'no'), nullable=False, server_default=text("'yes'"))
    forcename = Column(Enum('yes', 'no'), nullable=False, server_default=text("'no'"))
    forcegreetings = Column(Enum('yes', 'no'), nullable=False, server_default=text("'no'"))
    hidefromdir = Column(Enum('yes', 'no'), nullable=False, server_default=text("'yes'"))
    stamp = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    attachfmt = Column(String(10))
    searchcontexts = Column(Enum('yes', 'no'))
    cidinternalcontexts = Column(String(10))
    exitcontext = Column(String(10))
    volgain = Column(String(4))
    tempgreetwarn = Column(Enum('yes', 'no'), server_default=text("'yes'"))
    messagewrap = Column(Enum('yes', 'no'), server_default=text("'no'"))
    minpassword = Column(INTEGER(2), server_default=text("'4'"))
    vm_password = Column('vm-password', String(10))
    vm_newpassword = Column('vm-newpassword', String(10))
    vm_passchanged = Column('vm-passchanged', String(10))
    vm_reenterpassword = Column('vm-reenterpassword', String(10))
    vm_mismatch = Column('vm-mismatch', String(10))
    vm_invalid_password = Column('vm-invalid-password', String(10))
    vm_pls_try_again = Column('vm-pls-try-again', String(10))
    listen_control_forward_key = Column('listen-control-forward-key', String(2))
    listen_control_reverse_key = Column('listen-control-reverse-key', String(1))
    listen_control_pause_key = Column('listen-control-pause-key', String(1))
    listen_control_restart_key = Column('listen-control-restart-key', String(1))
    listen_control_stop_key = Column('listen-control-stop-key', String(13))
    backupdeleted = Column(String(3), server_default=text("'25'"))