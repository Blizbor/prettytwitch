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
    'BAN': re.compile(r'^:tmi\.twitch\.tv CLEARCHAT #(\w+) :(\w+)'),
    'CLEARCHAT': re.compile(r'^:tmi\.twitch\.tv CLEARCHAT #(\w+)'),
    'USERSTATE': re.compile(r'^:tmi\.twitch\.tv USERSTATE #(\w+)'),
    'ROOMSTATE': re.compile(r'^:tmi\.twitch\.tv ROOMSTATE #(\w+)'),
    'USERNOTICE': re.compile(r'^:tmi\.twitch\.tv USERNOTICE #(\w+) :(\.+)'),
    'GLOBALUSERSTATE': re.compile(r'^:tmi\.twitch\.tv GLOBALUSERSTATE'),
}
