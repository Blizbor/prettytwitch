import re
from utils.const import TYPES


class Response:
    """Represents any form of response from IRC server.

    Supported Operations:

    +-----------+------------------------------------------------+
    | Operation |                 Description                    |
    +===========+================================================+
    | str(x)    | Returns pretty representation of the response. |
    +-----------+------------------------------------------------+
    | repr(x)   | Returns raw representation of the response.    |
    +-----------+------------------------------------------------+

    Attributes
    -----------
    raw_msg : str
        Raw message response from Twitch IRC server.
    """

    def __init__(self, raw_msg: str):
        self.raw_msg = raw_msg

        # Detect and separate TAGS
        tags_pattern = re.compile(r'^@(\S+) :.+')
        tags_part = re.compile(r'^@(\S+) ')
        inspection = re.search(tags_pattern, self.raw_msg)
        if inspection is not None:
            used_part = tags_part.sub('', self.raw_msg)
            tags = dict()
            for pair in inspection.group(1).split(';'):
                tags[str(pair.split('=')[0])] = str(pair.split('=')[1])
            self.tags = tags.copy()
        else:
            used_part = self.raw_msg

        # Define the type
        for rtype, patt in TYPES.items():
            inspection = re.search(patt, used_part)
            self.type = 'UNDEFINED'
            if inspection is not None:
                self.type = rtype
                if rtype == 'CONNECTION':
                    self.code = inspection.group(1)
                    self.user = inspection.group(2)
                    self.message = inspection.group(3)
                elif rtype == 'USER_LIST':
                    self.code = '353'
                    self.user = inspection.group(1)
                    self.channel = inspection.group(2)
                    self.viewers = []
                    for user in (inspection.group(3)).split(' '):
                        self.viewers.append(user)
                    self.viewers.sort()
                elif rtype == 'USER_LIST_END':
                    self.code = '366'
                    self.message = 'End of /NAMES list'
                elif rtype == 'INVALID_CMD':
                    self.code = '421'
                    self.user = inspection.group(1)
                    self.command = inspection.group(2)
                elif rtype == 'CAPABILITY_REG':
                    if inspection.group(1) == 'ACK':
                        self.success = True
                    elif inspection.group(1) == 'NAK':
                        self.success = False
                    else:
                        continue
                    self.capability = inspection.group(2)
                elif rtype in ['JOIN', 'PART']:
                    self.user = inspection.group(1)
                    self.channel = inspection.group(2)
                elif rtype == 'PRIVMSG':
                    self.user = inspection.group(1)
                    self.channel = inspection.group(2)
                    self.message = inspection.group(3)
                elif rtype in ['OP', 'DEOP']:
                    self.channel = inspection.group(1)
                    self.user = inspection.group(2)
                elif rtype == 'NOTICE':
                    self.notice_id = inspection.group(1)
                    self.channel = inspection.group(2)
                    self.message = inspection.group(3)
                elif rtype == 'HOSTSTART':
                    self.channel = inspection.group(1)
                    self.target_channel = inspection.group(2)
                    self.viewers = inspection.group(3)
                elif rtype == 'HOSTEND':
                    self.channel = inspection.group(1)
                    self.viewers = inspection.group(2)
                elif rtype == 'BAN':
                    self.channel = inspection.group(1)
                    self.target_user = inspection.group(2)
                elif rtype == 'CLEARCHAT':
                    self.channel = inspection.group(1)
                elif rtype in ['USERSTATE', 'ROOMSTATE']:
                    self.channel = inspection.group(1)
                elif rtype == 'USERNOTICE':
                    self.channel = inspection.group(1)
                    self.message = inspection.group(2)
                elif rtype == 'GLOBALUSERSTATE':
                    pass

    def __str__(self):
        return getattr(self, 'pretty_message', None) or getattr(self, 'message', None) or self.raw_msg

    def __repr__(self):
        return self.raw_msg
