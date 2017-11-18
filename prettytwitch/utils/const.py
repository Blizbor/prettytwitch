import re

TYPES = {
    # System Messages
    'CONNECTION': re.compile(r'^:tmi\.twitch\.tv ([0-9]+) (\w+) :(.+)\r\n'),
    'USER_LIST': re.compile(r'^:\w+\.tmi\.twitch\.tv 353 (\w+) = #(\w+) :(\.+)\r\n'),
    'USER_LIST_END': re.compile(r'^:\w+\.tmi\.twitch\.tv 366 (\w+) #(\w+) :End of /NAMES list\r\n'),
    'RECONNECT': re.compile(r'^:tmi\.twitch\.tv RECONNECT\r\n'),

    # Invalid IRC Command
    'INVALID_CMD': re.compile(r'^:tmi\.twitch\.tv 421 (\w+) (\w+):Unknown command\r\n'),

    # Twitch specific IRC Requests
    'CAPABILITY_REG': re.compile(r'^:tmi\.twitch\.tv CAP \* ([AN][CA]K) :(.+)\r\n'),

    # Generic
    'JOIN': re.compile(r'^:(\w+)!\w+@\w+\.tmi\.twitch\.tv JOIN #(\w+)\r\n'),
    'PART': re.compile(r'^:(\w+)!\w+@\w+\.tmi\.twitch\.tv PART #(\w+)\r\n'),
    'PRIVMSG': re.compile(r'^:(\w+)!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #(\w+) :(.*)\r\n'),

    # Capability: Membership
    'OP': re.compile(r'^:jtv MODE #(\w+) \+o (\w)\r\n'),
    'DEOP': re.compile(r'^:jtv MODE #(\w+) -o (\w)\r\n'),

    # Capability: Commands
    'NOTICE': re.compile(r'^@msg-id=(\w+) :tmi\.twitch\.tv NOTICE #(\w+) :(\.+)\r\n'),
    'HOSTSTART': re.compile(r'^:tmi\.twitch\.tv HOSTTARGET #(\w+) :(\w+) ([0-9]+)\r\n'),
    'HOSTEND': re.compile(r'^:tmi\.twitch\.tv HOSTTARGET #(\w+) :- ([0-9]+)\r\n'),
    'BAN': re.compile(r'^:tmi\.twitch\.tv CLEARCHAT #(\w+) :(\w+)\r\n'),
    'CLEARCHAT': re.compile(r'^:tmi\.twitch\.tv CLEARCHAT #(\w+)\r\n'),
    'USERSTATE': re.compile(r'^:tmi\.twitch\.tv USERSTATE #(\w+)\r\n'),
    'ROOMSTATE': re.compile(r'^:tmi\.twitch\.tv ROOMSTATE #(\w+)\r\n'),
    'USERNOTICE': re.compile(r'^:tmi\.twitch\.tv USERNOTICE #(\w+)\r\n'),
    'SUB': re.compile(r'^:tmi\.twitch\.tv USERNOTICE #(\w+) :(\.+)\r\n'),
    'GLOBALUSERSTATE': re.compile(r'^:tmi\.twitch\.tv GLOBALUSERSTATE\r\n')
}

PMESSAGE_FORMAT = {
    # System Messages
    'CONNECTION': 'SERVER MESSAGE: {0.message}',
    'USER_LIST': 'LIST OF ONLINE USERS FOR #{0.channel}: {0.pviewers}',
    'USER_LIST_END': '--End of the viewer list--',
    'RECONNECT': 'ATTENTION: SERVERS ARE RESTARTING! RECONNECT IMMEDIATELY!',

    # Invalid IRC Command
    'INVALID_CMD': 'COMMAND \'{0.command}\' IS INVALID.',

    # Twitch specific IRC Requests
    'CAPABILITY_REG': 'YOUR REQUEST FOR {0.capability} WAS {0.psuccess}',

    # Generic
    'JOIN': 'USER {0.user} HAS JOINED #{0.channel}',
    'PART': 'USER {0.user} HAS LEFT #{0.channel}',
    'PRIVMSG': '#{0.channel} {0.user}: {0.message}',

    # Capability: Membership
    'OP': 'USER {0.user} HAS BEEN MODDED IN #{0.channel}',
    'DEOP': 'USER {0.user} HAS BEEN UNMODDED IN #{0.channel}',

    # Capability: Commands
    'NOTICE': 'NOTICE! #{0.channel}: {0.message}',
    'HOSTSTART': '{0.channel} IS NOW HOSTING {0.target_channel} WITH {0.viewers} VIEWERS',
    'HOSTEND': '{0.channel} HAS FINISHED HOSTING WITH {0.viewers} VIEWERS',
    'BAN': '{0.user} HAS BEEN BANNED FROM #{0.channel}',
    'TIMEOUT': '{0.user} HAS BEEN TIMED OUT FROM #{0.channel} FOR {0.ban_duration} SECONDS',
    'USERSTATE': 'YOU HAVE SUCCESSFULLY LOGGED IN',
    'ROOMSTATE': '#{0.channel} SETTINGS HAVE CHANGED',
    'USERNOTICE': 'YOU ARE BEING RAIDED BY {0.channel}',
    'SUB': 'SOMEONE HAVE SUBSCRIBED TO {0.channel}: {0.message}',
    'GLOBALUSERSTATE': 'YOU HAVE SUCCESSFULLY LOGGED IN'
}
