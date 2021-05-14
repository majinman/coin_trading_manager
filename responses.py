import codes

# Responses

NOT_FOUND = {
                    "message": "NOT_FOUND",
                   "error_code": codes.UNAUTORIZED_ERROR_CODE,
                   "is_success": False
               }, 404

UNAUTHORIZED = {
                   "message": "Permission denied",
                   "error_code": codes.UNAUTORIZED_ERROR_CODE,
                   "is_success": False
               }, 401

INVALID_PARAMETERS = {
                         "message": "Invalid parameters.",
                         "error_code": codes.INVALID_PARAMETERS,
                         "is_success": False
                     }, 400

EMAIL_OR_NICKNAME_ALREADY_EXISTS = {
                                       "message": "Email or Nickname already exists",
                                       "error_code": codes.EMAIL_OR_NICKNAME_ALREADY_EXISTS,
                                       "is_success": False
                                   }, 400

QUERY_NOT_EXISTS = {
                       "message": "Query not exists.",
                       "error_code": codes.QUERY_NOT_EXISTS,
                       "is_success": False
                   }, 400

INVALID_TOKEN = {
                    "message": "Invalid Token.",
                    "error_code": codes.INVALID_TOKEN,
                    "is_success": False
                }, 400

ALREADY_EXISTS = {
                     "message": "already exists.",
                     "error_code": codes.ALREADY_EXISTS,
                     "is_success": False
                 }, 400

DUPLICATE_MEMBERSHIP = {
                    "message": "already same key exists.",
                     "error_code": codes.DUPLICATE_MEMBERSHIP,
                     "is_success": False
}, 400

TEST_REQUIRED = {
    "message": "needs test history",
    "error_code": codes.TEST_REQUIRED,
    "is_success": False
}

PARTNER_TEST_REQUIRED = {
    "message": "needs test history",
    "error_code": codes.PARTNER_TEST_REQUIRED,
    "is_success": False
}

STORY_REQUIRED = {
    "message": "needs story history",
    "error_code": codes.STORY_REQUIRED,
    "is_success": False
}

PROFILE_REQUIRED = {
    "message": "needs profile filled",
    "error_code": codes.PROFILE_INCOMPLETE,
    "is_success": False
}

PROFILE_DISAPPROVED = {
    "message": "needs profile approaved",
    "error_code": codes.PROFILE_NOT_APPROVED,
    "is_success": False
}


CHAT_LIMIT = {
    "message": "reach chat limit",
    "error_code": codes.CHAT_LIMIT,
    "is_success": False
}

GPS_ABUSING = {
    "message": "GPS abusing.",
    "error_code": codes.GPS_ABUSING,
    "is_success": False
}

SELF_CHATTING = {
    "message": "self chatting not allowed.",
    "error_code": codes.SELF_CHATTING,
    "is_success": False
}

MATCHING_REQUIRED = {
    "message": "needs matching history.",
    "error_code": codes.MATCHING_REQUIRED,
    "is_success": False
}

MATCH_EXIST = {
    "message": "match exist.",
    "error_code": codes.MATCH_EXIST,
    "is_success": False
}

ALREADY_DONE = {
    "message": "already done before.",
    "error_code": codes.ALREADY_DONE,
    "is_success": False
}

NOT_EMAIL_AUTHENTICATED = {
    "messages": "not email authenticated",
    "error_code": codes.NOT_EMAIL_AUTHENTICATED,
    "is_success": False
}

NOT_SELF_AUTHENTICATED = {
    "messages": "not self authenticated",
    "error_code": codes.NOT_SELF_AUTHENTICATED,
    "is_success": False
}

STORY_NOT_REVIEWED = {
    "messages": "story not reviewed",
    "error_code": codes.STORY_NOT_REVIEWED,
    "is_success": False
}

NOT_FILLED_INFORMATION = {
    "messages": "not information filled",
    "error_code": codes.NOT_FILLED_INFORMATION,
    "is_success": False
}

INVALID_CODE_TYPE = {
    "messages": "not valid code for user sex",
    "error_code": codes.INVALID_CODE_TYPE,
    "is_success": False
}

NOT_ENOUGH_POOL = {
    "messages": "not enough users in pool",
    "error_code": codes.NOT_ENOUGH_USERS,
    "is_success": False
}

NOT_HUNDRED_USERS = {
    "messages": "not enough users in pool",
    "error_code": codes.NOT_HUNDRED_USERS,
    "is_success": False
}


NOT_ENOUGH_BRIDGE = {
    "messages": "not enough bridge",
    "error_code": codes.NOT_ENOUGH_BRIDGE,
    "is_success": False
}

NOT_ENOUGH_TIME = {
    "messages": "not enough time to terminate chat",
    "error_code": codes.NOT_ENOUGH_TIME,
    "is_success": False
}

NO_CHARACTERISTIC = {
    "messages": "not especially characteristic",
    "error_code": codes.NO_CHARACTERISTIC,
    "is_success": False
}

NOT_KNOWN_ERROR = {
    "messages": "not known error",
    "error_code": codes.NOT_KNOWN_ERROR,
    "is_success": False
}

OVER_REPORT_USER = {
    "messages": "reported over limit",
    "error_code": codes.OVER_REPORT_USER,
    "is_success": False
}

LEFT_USER = {
    "messages": "left user",
    "error_code": codes.LEFT_USER,
    "is_success": False
}


SUCCESS = {
    "is_success": True
}

CREATED_SUCCESS = {
    "is_success": True
}, 201
