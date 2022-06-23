from dbm import dumb
import requests
import json

def get_data():

    cookies = {
        '__lhash_': '51c9510c70262b4f370027e2f7e0d015',
        'COMPARISON_INDICATOR': 'false',
        'MAIN_PAGE_VARIATION_1': '2',
        'MVID_2_exp_in_1': '1',
        'MVID_AB_SERVICES_DESCRIPTION': 'var4',
        'MVID_ADDRESS_COMMENT_AB_TEST': '2',
        'MVID_BLACK_FRIDAY_ENABLED': 'true',
        'MVID_CATALOG_STATE': '1',
        'MVID_CHECKOUT_REGISTRATION_AB_TEST': '2',
        'MVID_FILTER_CODES': 'true',
        'MVID_FILTER_TOOLTIP': '1',
        'MVID_FLOCKTORY_ON': 'true',
        'MVID_GEOLOCATION_NEEDED': 'true',
        'MVID_GET_LOCATION_BY_DADATA': 'DaData',
        'MVID_GIFT_KIT': 'true',
        'MVID_IS_NEW_BR_WIDGET': 'true',
        'MVID_KLADR_ID': '6600000100000',
        'MVID_LAYOUT_TYPE': '1',
        'MVID_NEW_ACCESSORY': 'true',
        'MVID_NEW_DESKTOP_FILTERS': 'true',
        'MVID_NEW_LK': 'true',
        'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
        'MVID_NEW_LK_LOGIN': 'true',
        'MVID_NEW_LK_MENU_BUTTON': 'true',
        'MVID_NEW_LK_OTP_TIMER': 'true',
        'MVID_NEW_MBONUS_BLOCK': 'true',
        'MVID_NEW_SUGGESTIONS': 'true',
        'MVID_PROMO_CATALOG_ON': 'true',
        'MVID_REGION_SHOP': 'S953',
        'MVID_SERVICES': '111',
        'MVID_SERVICES_MINI_BLOCK': 'var2',
        'MVID_TAXI_DELIVERY_INTERVALS_VIEW': 'new',
        'MVID_TIMEZONE_OFFSET': '5',
        'MVID_WEBP_ENABLED': 'true',
        'NEED_REQUIRE_APPLY_DISCOUNT': 'true',
        'PROMOLISTING_WITHOUT_STOCK_AB_TEST': '2',
        'flacktory': 'no',
        'wurfl_device_id': 'generic_web_browser',
        'MVID_NEW_OLD': 'eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9',
        'MVID_OLD_NEW': 'eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==',
        'BIGipServeratg-ps-prod_tcp80': '2919554058.20480.0000',
        'bIPs': '1595647062',
        'SL_G_WPT_TO': 'ru',
        'popmechanic_sbjs_migrations': 'popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1',
        '__SourceTracker': 'google__organic',
        'admitad_deduplication_cookie': 'google__organic',
        'SMSError': '',
        'authError': '',
        'tmr_lvidTS': '1655826307300',
        'tmr_lvid': '3e20cacc21de0baeff2570a527977f50',
        '_gid': 'GA1.2.1337716569.1655826307',
        'SL_wptGlobTipTmp': '1',
        'SL_GWPT_Show_Hide_tmp': '1',
        '_ym_uid': '1655826308276237788',
        '_ym_d': '1655826308',
        'st_uid': 'd6c8ad9a389a346ee5ac13c5b83ef09a',
        'advcake_track_id': 'e9a0ea4f-0792-315a-7f4c-f4c4e5a67294',
        'advcake_session_id': 'e673a5a8-ec68-d8ef-bdea-d457949d47d8',
        'HINTS_FIO_COOKIE_NAME': '2',
        'JSESSIONID': '6my8vxnC2B015BMR7LPThTL25rKw1d4ntjtMQvf8WfCg2Mc42f61!400565351',
        'MVID_CALC_BONUS_RUBLES_PROFIT': 'false',
        'MVID_CART_MULTI_DELETE': 'false',
        'MVID_CITY_ID': 'CityCZ_2030',
        'MVID_GUEST_ID': '20920557444',
        'MVID_LP_SOLD_VARIANTS': '0',
        'MVID_REGION_ID': '5',
        'PRESELECT_COURIER_DELIVERY_FOR_KBT': 'true',
        'searchType2': '3',
        '_ym_isad': '1',
        'afUserId': '6297833e-b621-4d09-bbdd-46c8a1001ee3-p',
        'flocktory-uuid': '05ac0836-eec7-422d-a1e1-38335a0bf96f-8',
        'uxs_uid': '20d8f8f0-f179-11ec-8f39-1179865a62fa',
        'AF_SYNC': '1655826308647',
        'BIGipServeratg-ps-prod_tcp80_clone': '2919554058.20480.0000',
        'MVID_GTM_BROWSER_THEME': '1',
        'deviceType': 'desktop',
        '__zzatgib-w-mvideo': 'MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2UveDYlLRcfMkVnTXoqKy4hcj9vK0N/WUNyPUQKZlFjDSVZD3JuR1shODV+WlEkPl8/d3N0Gj9lHWRNXiJIVj56Kx4Wf20pUn8RY0BBX28beyJfKggkYzVfGUNqTg1pN1wUPHVlPkdyeDE9ayBgTmAgSVE/SF5dSRIyYhJAQE1HDTdAXjdXYTAPFhFNRxU9VlJPQyhrG3FYMA==p2Eikg==',
        '__zzatgib-w-mvideo': 'MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2UveDYlLRcfMkVnTXoqKy4hcj9vK0N/WUNyPUQKZlFjDSVZD3JuR1shODV+WlEkPl8/d3N0Gj9lHWRNXiJIVj56Kx4Wf20pUn8RY0BBX28beyJfKggkYzVfGUNqTg1pN1wUPHVlPkdyeDE9ayBgTmAgSVE/SF5dSRIyYhJAQE1HDTdAXjdXYTAPFhFNRxU9VlJPQyhrG3FYMA==p2Eikg==',
        'cfidsgib-w-mvideo': 'ihm8+iZ/rMi94DuuFtOLeoL/M25cEwPltJQy4X+mAqX5Jw6xPb9pxmpDNy6iXpG8D0raP531IOQNp/4WxsfF4oxh7lWRxCjEzMDpWQRNircq9S49rMNJNQRdRZM45evKhrAeLWnzc1IwoBIidM7G2Q6tHYuljKDhV/3t',
        'cfidsgib-w-mvideo': 'ihm8+iZ/rMi94DuuFtOLeoL/M25cEwPltJQy4X+mAqX5Jw6xPb9pxmpDNy6iXpG8D0raP531IOQNp/4WxsfF4oxh7lWRxCjEzMDpWQRNircq9S49rMNJNQRdRZM45evKhrAeLWnzc1IwoBIidM7G2Q6tHYuljKDhV/3t',
        'gsscgib-w-mvideo': 'mdb/vaA3rPKMVjwGdiUtcM8lzXW30dH9RzNAjatEckTYOJLNxMKm86UOwbpOTiZyK2M2Hk/stKR9jyBERX7/4oAw/ur9HWdnLxlHc6CpEXgw3IqUECHyrQl94bZfgxXaWhmEQzmtbWgZvxySXzdNuSUvn1kKquusJfBZD7WS/CRgNJXhdGkrBinL80RH9NfKlW/5OiObudHbvO/0DHWK41+QgpNJAjMTcb5UEx4jIddAYQHNA01JV7BNNr0cEA==',
        'gsscgib-w-mvideo': 'mdb/vaA3rPKMVjwGdiUtcM8lzXW30dH9RzNAjatEckTYOJLNxMKm86UOwbpOTiZyK2M2Hk/stKR9jyBERX7/4oAw/ur9HWdnLxlHc6CpEXgw3IqUECHyrQl94bZfgxXaWhmEQzmtbWgZvxySXzdNuSUvn1kKquusJfBZD7WS/CRgNJXhdGkrBinL80RH9NfKlW/5OiObudHbvO/0DHWK41+QgpNJAjMTcb5UEx4jIddAYQHNA01JV7BNNr0cEA==',
        'fgsscgib-w-mvideo': 'MshVc27a83654577b3fe469d44bdcb065c284680',
        'fgsscgib-w-mvideo': 'MshVc27a83654577b3fe469d44bdcb065c284680',
        'cfidsgib-w-mvideo': 'yju3nEDz1msIo4ctb1b3jLP7MvKQvCUSEiGF0hFGFRn+AxZL9qIhhyVlKeBOBxrxXWfKoHR/URMu1s9wf8JPA0LO3fyVlHAZXuQAD045CyazhM8KtTy3mO+y+UsTkP+35nkXrKOQspP2MJLqlffuUJBAD5lBc64Xn998',
        'CACHE_INDICATOR': 'false',
        'mindboxDeviceUUID': 'eb76b74e-646d-42d8-93da-da4a7b3a798b',
        'directCrm-session': '%7B%22deviceGuid%22%3A%22eb76b74e-646d-42d8-93da-da4a7b3a798b%22%7D',
        '_ga': 'GA1.2.1851698169.1655826307',
        'tmr_detect': '1%7C1655826422309',
        'tmr_reqNum': '53',
        'MVID_ENVCLOUD': 'primary',
        '_ga_CFMZTSS5FM': 'GS1.1.1655830656.2.0.1655830656.0',
        '_ga_BNX5WPP3YK': 'GS1.1.1655830656.2.0.1655830656.60',
        '_dc_gtm_UA-1873769-1': '1',
        '_dc_gtm_UA-1873769-37': '1',
        'ADRUM_BT': 'R:126|g:b4651416-360c-442d-9c63-d2b01b2d02a21514952|h:e',
    }

    headers = {
        'authority': 'www.mvideo.ru',
        'accept': 'application/json',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'no-cache',
        # Requests sorts cookies= alphabetically
        # 'cookie': '__lhash_=51c9510c70262b4f370027e2f7e0d015; COMPARISON_INDICATOR=false; MAIN_PAGE_VARIATION_1=2; MVID_2_exp_in_1=1; MVID_AB_SERVICES_DESCRIPTION=var4; MVID_ADDRESS_COMMENT_AB_TEST=2; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CATALOG_STATE=1; MVID_CHECKOUT_REGISTRATION_AB_TEST=2; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GEOLOCATION_NEEDED=true; MVID_GET_LOCATION_BY_DADATA=DaData; MVID_GIFT_KIT=true; MVID_IS_NEW_BR_WIDGET=true; MVID_KLADR_ID=6600000100000; MVID_LAYOUT_TYPE=1; MVID_NEW_ACCESSORY=true; MVID_NEW_DESKTOP_FILTERS=true; MVID_NEW_LK=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_LOGIN=true; MVID_NEW_LK_MENU_BUTTON=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_NEW_SUGGESTIONS=true; MVID_PROMO_CATALOG_ON=true; MVID_REGION_SHOP=S953; MVID_SERVICES=111; MVID_SERVICES_MINI_BLOCK=var2; MVID_TAXI_DELIVERY_INTERVALS_VIEW=new; MVID_TIMEZONE_OFFSET=5; MVID_WEBP_ENABLED=true; NEED_REQUIRE_APPLY_DISCOUNT=true; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; flacktory=no; wurfl_device_id=generic_web_browser; MVID_NEW_OLD=eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9; MVID_OLD_NEW=eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==; BIGipServeratg-ps-prod_tcp80=2919554058.20480.0000; bIPs=1595647062; SL_G_WPT_TO=ru; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; __SourceTracker=google__organic; admitad_deduplication_cookie=google__organic; SMSError=; authError=; tmr_lvidTS=1655826307300; tmr_lvid=3e20cacc21de0baeff2570a527977f50; _gid=GA1.2.1337716569.1655826307; SL_wptGlobTipTmp=1; SL_GWPT_Show_Hide_tmp=1; _ym_uid=1655826308276237788; _ym_d=1655826308; st_uid=d6c8ad9a389a346ee5ac13c5b83ef09a; advcake_track_id=e9a0ea4f-0792-315a-7f4c-f4c4e5a67294; advcake_session_id=e673a5a8-ec68-d8ef-bdea-d457949d47d8; HINTS_FIO_COOKIE_NAME=2; JSESSIONID=6my8vxnC2B015BMR7LPThTL25rKw1d4ntjtMQvf8WfCg2Mc42f61!400565351; MVID_CALC_BONUS_RUBLES_PROFIT=false; MVID_CART_MULTI_DELETE=false; MVID_CITY_ID=CityCZ_2030; MVID_GUEST_ID=20920557444; MVID_LP_SOLD_VARIANTS=0; MVID_REGION_ID=5; PRESELECT_COURIER_DELIVERY_FOR_KBT=true; searchType2=3; _ym_isad=1; afUserId=6297833e-b621-4d09-bbdd-46c8a1001ee3-p; flocktory-uuid=05ac0836-eec7-422d-a1e1-38335a0bf96f-8; uxs_uid=20d8f8f0-f179-11ec-8f39-1179865a62fa; AF_SYNC=1655826308647; BIGipServeratg-ps-prod_tcp80_clone=2919554058.20480.0000; MVID_GTM_BROWSER_THEME=1; deviceType=desktop; __zzatgib-w-mvideo=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2UveDYlLRcfMkVnTXoqKy4hcj9vK0N/WUNyPUQKZlFjDSVZD3JuR1shODV+WlEkPl8/d3N0Gj9lHWRNXiJIVj56Kx4Wf20pUn8RY0BBX28beyJfKggkYzVfGUNqTg1pN1wUPHVlPkdyeDE9ayBgTmAgSVE/SF5dSRIyYhJAQE1HDTdAXjdXYTAPFhFNRxU9VlJPQyhrG3FYMA==p2Eikg==; __zzatgib-w-mvideo=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2UveDYlLRcfMkVnTXoqKy4hcj9vK0N/WUNyPUQKZlFjDSVZD3JuR1shODV+WlEkPl8/d3N0Gj9lHWRNXiJIVj56Kx4Wf20pUn8RY0BBX28beyJfKggkYzVfGUNqTg1pN1wUPHVlPkdyeDE9ayBgTmAgSVE/SF5dSRIyYhJAQE1HDTdAXjdXYTAPFhFNRxU9VlJPQyhrG3FYMA==p2Eikg==; cfidsgib-w-mvideo=ihm8+iZ/rMi94DuuFtOLeoL/M25cEwPltJQy4X+mAqX5Jw6xPb9pxmpDNy6iXpG8D0raP531IOQNp/4WxsfF4oxh7lWRxCjEzMDpWQRNircq9S49rMNJNQRdRZM45evKhrAeLWnzc1IwoBIidM7G2Q6tHYuljKDhV/3t; cfidsgib-w-mvideo=ihm8+iZ/rMi94DuuFtOLeoL/M25cEwPltJQy4X+mAqX5Jw6xPb9pxmpDNy6iXpG8D0raP531IOQNp/4WxsfF4oxh7lWRxCjEzMDpWQRNircq9S49rMNJNQRdRZM45evKhrAeLWnzc1IwoBIidM7G2Q6tHYuljKDhV/3t; gsscgib-w-mvideo=mdb/vaA3rPKMVjwGdiUtcM8lzXW30dH9RzNAjatEckTYOJLNxMKm86UOwbpOTiZyK2M2Hk/stKR9jyBERX7/4oAw/ur9HWdnLxlHc6CpEXgw3IqUECHyrQl94bZfgxXaWhmEQzmtbWgZvxySXzdNuSUvn1kKquusJfBZD7WS/CRgNJXhdGkrBinL80RH9NfKlW/5OiObudHbvO/0DHWK41+QgpNJAjMTcb5UEx4jIddAYQHNA01JV7BNNr0cEA==; gsscgib-w-mvideo=mdb/vaA3rPKMVjwGdiUtcM8lzXW30dH9RzNAjatEckTYOJLNxMKm86UOwbpOTiZyK2M2Hk/stKR9jyBERX7/4oAw/ur9HWdnLxlHc6CpEXgw3IqUECHyrQl94bZfgxXaWhmEQzmtbWgZvxySXzdNuSUvn1kKquusJfBZD7WS/CRgNJXhdGkrBinL80RH9NfKlW/5OiObudHbvO/0DHWK41+QgpNJAjMTcb5UEx4jIddAYQHNA01JV7BNNr0cEA==; fgsscgib-w-mvideo=MshVc27a83654577b3fe469d44bdcb065c284680; fgsscgib-w-mvideo=MshVc27a83654577b3fe469d44bdcb065c284680; cfidsgib-w-mvideo=yju3nEDz1msIo4ctb1b3jLP7MvKQvCUSEiGF0hFGFRn+AxZL9qIhhyVlKeBOBxrxXWfKoHR/URMu1s9wf8JPA0LO3fyVlHAZXuQAD045CyazhM8KtTy3mO+y+UsTkP+35nkXrKOQspP2MJLqlffuUJBAD5lBc64Xn998; CACHE_INDICATOR=false; mindboxDeviceUUID=eb76b74e-646d-42d8-93da-da4a7b3a798b; directCrm-session=%7B%22deviceGuid%22%3A%22eb76b74e-646d-42d8-93da-da4a7b3a798b%22%7D; _ga=GA1.2.1851698169.1655826307; tmr_detect=1%7C1655826422309; tmr_reqNum=53; MVID_ENVCLOUD=primary; _ga_CFMZTSS5FM=GS1.1.1655830656.2.0.1655830656.0; _ga_BNX5WPP3YK=GS1.1.1655830656.2.0.1655830656.60; _dc_gtm_UA-1873769-1=1; _dc_gtm_UA-1873769-37=1; ADRUM_BT=R:126|g:b4651416-360c-442d-9c63-d2b01b2d02a21514952|h:e',
        'pragma': 'no-cache',
        'referer': 'https://www.mvideo.ru/noutbuki-planshety-komputery-8/noutbuki-118/f/skidka=da/tolko-v-nalichii=da/diagonal-ekrana=17-i-bolee,ot-15-do-169',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        'x-set-application-id': 'cfcbe20e-2b24-4639-8907-b2d39f1c0cce',
    }

    params = {
        'categoryId': '118',
        'offset': '0',
        'limit': '24',
        'filterParams': [
            'WyLQotC+0LLQsNGA0Ysg0YHQviDRgdC60LjQtNC60L7QuSIsIi04Iiwi0JHQvtC70LXQtSA1JSJd',
            'WyLQotC+0LvRjNC60L4g0LIg0L3QsNC70LjRh9C40LgiLCItOSIsItCU0LAiXQ==',
            'WyLQlNC40LDQs9C+0L3QsNC70Ywg0Y3QutGA0LDQvdCwIiwiNjEyNDk1IiwiMTcg0Lgg0LHQvtC70LXQtSIsItC+0YIgMTUg0LTQviAxNi45Il0=',
        ],
    }

    response = requests.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies, headers=headers).json()
    # print(response)
    products_ids=response.get('body').get('products')

    with open('1_products_ids.json', 'w') as file:
        json.dump(products_ids, file, indent=4, ensure_ascii=False)
    # print(products_ids)

    json_data = {
    'productIds': products_ids,
    'mediaTypes': [
        'images',
    ],
    'category': True,
    'status': True,
    'brand': True,
    'propertyTypes': [
        'KEY',
    ],
    'propertiesConfig': {
        'propertiesPortionSize': 5,
    },
    'multioffer': False,}

    response = requests.post('https://www.mvideo.ru/bff/product-details/list', cookies=cookies, headers=headers, json=json_data).json()
    with open('2_items.json', 'w', encoding='utf-8') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)
    
    # print(len(response.get('body').get('products')))

    products_ids_str=','.join(products_ids)

    params = {
        'productIds': products_ids_str,
        'addBonusRubles': 'true',
        'isPromoApplied': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/prices', params=params, cookies=cookies, headers=headers).json()
    
    with open('3_prices.json', 'w', encoding='utf-8') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

    items_prices={}

    material_prices=response.get('body').get('materialPrices')

    for item in material_prices:
        item_id=item.get('productId')
        item_baseprice=item.get('price').get('basePrice')
        item_saleprice=item.get('price').get('salePrice')
        item_bonus=item.get('bonusRubles').get('total')

        items_prices[item_id]={
            'basePrice':item_baseprice,
            'salePrice':item_saleprice,
            'item_bonus':item_bonus
        }
    
    with open('4_item_prices.json', 'w', encoding='utf-8') as file:
        json.dump(items_prices, file, indent=4, ensure_ascii=False)

def get_result():
    with open('2_items.json', encoding='utf-8') as file:
        products_data=json.load(file)

    with open('4_item_prices.json', encoding='utf-8') as file:
        products_prices=json.load(file)

    products_data=products_data.get('body').get('products')

    for item in products_data:
        products_id=item.get('productId')

        if products_id in products_prices:
            prices=products_prices[products_id]

        item['item_basePrice']=prices.get('basePrice')
        item['item_salePrice']=prices.get('salePrice')
        item['item_bonus']=prices.get('item_bonus')

    with open('5_result.json', 'w', encoding='utf-8') as file:
        json.dump(products_data, file, indent=4, ensure_ascii=False)

get_data()
get_result()