# -*- coding: utf-8 -*-
#
## This file is part of Invenio.
## Copyright (C) 2012 CERN.
##
## Invenio is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 2 of the
## License, or (at your option) any later version.
##
## Invenio is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with Invenio; if not, write to the Free Software Foundation, Inc.,
## 59 Temple Place, Suite 330, Boston, MA 02D111-1307, USA.

"""
inveniocfg_upgrade database model.
"""

# General imports.
from invenio.sqlalchemyutils import db

# Create your models here.

class Upgrade(db.Model):
    """Represents an Upgrade record."""
    __tablename__ = 'upgrade'

    upgrade = db.Column(db.String(255), primary_key=True, nullable=False)
    applied = db.Column(db.DateTime, nullable=False)

