# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class PhoneNumberValidatorPartner(models.Model):
    _inherit = ['res.partner']

    phone = fields.Char('Phone Number', default='+966 5X XXX XXXX', required=True)
   
    

    @api.constrains('phone')
    def number_check(self):
        if len(self.phone) < 16:
            raise ValidationError("Phone number should be 16 Digits")

        elif len(self.phone) > 16:   
            raise ValidationError("Phone number should not exceed 16 Digits")

        elif len(self.phone) == 16:
            # check the phone numebr without country code in database for possible duplicate creations
            without_ccode = self.phone
            without_ccode = without_ccode[5:16]
            without_ccode = without_ccode.replace(" ", "")
            without_ccode = '0' + without_ccode
            number_exists = self.env['res.partner'].search(['|', ('phone' , '=' , self.phone) , ('phone' , '=' , without_ccode)], count=True)
            if number_exists != True:
                raise ValidationError("Contact Number %s Already Exists" % self.phone)
                
      

            



