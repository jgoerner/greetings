#!/usr/bin/env python

GREETING_DICT = {"EN": ["Hello", "How are you"],
                 "DE": ["Hallo", "Wie geht es dir"],
                 "ZH": ["Ni hao", "Ni hao ma"]}


def greet(person, language='EN'):
    """Greet a person in a specific language

    Parameter
    ---------
    person: String,
        Person to be greeted
    language: String, default="EN"
        Language code in which to greet

    """
    if language not in GREETING_DICT.keys():
        raise ValueError(
            "{} is currently not supported, please use {}" .format(
                language, " ".join(
                    list(
                        GREETING_DICT.keys()))))

    greeting = "{} {}, {}".format(GREETING_DICT[language][0],
                                  person,
                                  GREETING_DICT[language][1])

    return greeting
