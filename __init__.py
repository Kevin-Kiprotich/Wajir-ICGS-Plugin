# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Wajir_ICGS
                                 A QGIS plugin
 A plugin for fetching data collected in the field.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2025-03-20
        copyright            : (C) 2025 by LocateIT, Kevin Kiprotich
        email                : kevinkiprotich0089@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

from qgis.PyQt import QtCore
from qgis.core import QgsMessageLog

debug = QtCore.QSettings().value('Wajir_ICGS/debug', True)
# log the details
def log(message, level=0):
    if debug:
        QgsMessageLog.logMessage(message, tag="Wajir_ICGS", level=level)

# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load Wajir_ICGS class from file Wajir_ICGS.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .plugin import Wajir_ICGS
    return Wajir_ICGS(iface)
