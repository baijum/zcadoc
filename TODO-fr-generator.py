from text_table import TextTable
from enum import Enum

TRANSLATED_STATUS = Enum("WIP", "Y", "N")
REREADED_STATUS = Enum("WIP", "Y", "N")
DONE_STATUS = Enum("Y", "N")
NOTE_LEVEL = Enum("-", "1", "2", "3", "4", "5")


heading_content = ("Chapter or section name", "TRANSLATED", "REREADED", "DONE", "NOTE")

table_content = (
    (" * Getting started",                          TRANSLATED_STATUS.WIP, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o Introduction",                       TRANSLATED_STATUS.Y, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]), 
    ("       o A brief history",                    TRANSLATED_STATUS.Y, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o Installation",                       TRANSLATED_STATUS.Y, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o Experimenting with code",            TRANSLATED_STATUS.Y, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    (" * An example",                               TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o Introduction",                       TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o Procedural approach",                TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o Object oriented approach",           TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o The adapter pattern",                TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    (" * Interfaces",                               TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o Introduction",                       TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o Declaring interfaces",               TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o Implementing interfaces",            TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o Example revisited",                  TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o Marker interfaces",                  TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o Invariants",                         TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    (" * Adapters",                                 TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o Implementation",                     TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o Registration",                       TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o Querying adapter",                   TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o Retrieving adapter using interface", TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o Adapter pattern",                    TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    (" * Utility",                                  TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o Introduction",                       TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o Simple utility",                     TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o Named utility",                      TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o Factory",                            TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    (" * Advanced adapters",                        TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o Multi adapter",                      TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o Subscription adapter",               TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o Handler",                            TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    (" * ZCA usage in Zope",                        TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o ZCML",                               TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o Overrides",                          TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o NameChooser",                        TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o LocationPhysicallyLocatable",        TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o DefaultSized",                       TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o ZopeVersionUtility",                 TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    (" * Reference",                                TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o Attribute",                          TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o Declaration",                        TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o Interface",                          TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o adapts",                             TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o alsoProvides",                       TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o classImplements",                    TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o classImplementsOnly",                TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o classProvides",                      TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o ComponentLookupError",               TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o createObject",                       TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o directlyProvidedBy",                 TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o directlyProvides",                   TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o getAdapter",                         TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o getAdapterInContext",                TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o getAdapters",                        TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o getAllUtilitiesRegisteredFor",       TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o getFactoriesFor",                    TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o getFactoryInterfaces",               TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o getGlobalSiteManager",               TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o getMultiAdapter",                    TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o getSiteManager",                     TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o getUtilitiesFor",                    TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o getUtility",                         TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o handle",                             TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o implementedBy",                      TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o implementer",                        TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o implements",                         TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o implementsOnly",                     TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o moduleProvides",                     TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o noLongerProvides",                   TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o provideAdapter",                     TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o provideHandler",                     TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o provideSubscriptionAdapter",         TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o provideUtility",                     TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o providedBy",                         TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o queryAdapter",                       TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o queryAdapterInContext",              TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o queryMultiAdapter",                  TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o queryUtility",                       TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o registerAdapter",                    TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o registeredAdapters",                 TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o registeredHandlers",                 TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o registeredSubscriptionAdapters",     TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o registeredUtilities",                TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o registerHandler",                    TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o registerSubscriptionAdapter",        TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o registerUtility",                    TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o subscribers",                        TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o unregisterAdapter",                  TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o unregisterHandler",                  TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o unregisterSubscriptionAdapter",      TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0]),
    ("       o unregisterUtility",                  TRANSLATED_STATUS.N, REREADED_STATUS.N, DONE_STATUS.N, NOTE_LEVEL[0])
)

column_greater_size_content = [0, 0, 0, 0, 0]

#summary_value = {
#    "TRANSLATED" : { "YES" : 0, "WIP": 0 },
#    "REREADED" :  { "YES" : 0 },
#    "DONE" : { "YES" : 0 }
#}

summary_value = {
    TRANSLATED_STATUS.Y : 0,
    TRANSLATED_STATUS.WIP : 0,
    REREADED_STATUS.Y : 0,
    REREADED_STATUS.WIP : 0,
    DONE_STATUS.Y: 0
}

for row in (heading_content,) + table_content:
    for col_index in range(0, len(row)):
        if (len(str(row[col_index])) > column_greater_size_content[col_index]):
            column_greater_size_content[col_index] = len(str(row[col_index]))
       
        if (summary_value.has_key(row[col_index])):
            summary_value[row[col_index]] = summary_value[row[col_index]] + 1

ascii_table_content = TextTable(
    *tuple([(column_greater_size_content[i], heading_content[i]) for i in range(0, 5)])
)

for row in table_content:
    ascii_table_content.row(*(((row[0]),) + tuple([str(row[col_index]).center(column_greater_size_content[col_index]) for col_index in range(1, len(row))])))


summary_content = (
    ("Translated", str(str(summary_value[TRANSLATED_STATUS.Y]) + " / " + str(len(table_content)) + " (" + str((summary_value[TRANSLATED_STATUS.Y] * 100) / len(table_content)) + " %) , " + str(summary_value[TRANSLATED_STATUS.WIP]) + " in WIP")),
    ("Rereaded", str(str(summary_value[REREADED_STATUS.Y]) + " / " + str(len(table_content)) + " (" + str((summary_value[REREADED_STATUS.Y] * 100) / len(table_content)) + " %) , " + str(summary_value[REREADED_STATUS.WIP]) + " in WIP")),
    ("Done", str(str(summary_value[DONE_STATUS.Y]) + " / " + str(len(table_content)) + " (" + str((summary_value[DONE_STATUS.Y] * 100) / len(table_content)) + " %)"))
)

ascii_summary_content = TextTable((12), (28))
for row in summary_content:
    ascii_summary_content.row(*row)

print(
"""
This file contain some informations about the growth of french
translation.

This file is generate by TODO-fr-generator.py script file.

Summary
=======
""")


print(ascii_summary_content.draw())

print("""
Detail table
============

Fields values :

 * Translated column can be Yes, No, WIP (Work In Progress)
 * Rereaded column can be Yes, No, WIP (Work In Progress)
 * Done column can be Yes, No
 * Note column can be "-" or 1 to 5, it's quality note

""")

print ascii_table_content.draw()


