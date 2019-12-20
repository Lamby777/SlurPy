class MetaException(Exception): pass
class JuiceFileException(Exception): pass
class SlurpException(Exception): pass
class SlurpSyntaxError(SlurpException): pass
class SlurpMathError(SlurpException): pass