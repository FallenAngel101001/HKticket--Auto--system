import time
from seleniumbase import page_actions


def check_pagen_is_match_or_not(sb):
    while True:
        sb.activate_jquery()
        data = sb.is_element_enabled('#p', by="css selector")
        entry = sb.is_element_enabled(
            '#ctl00_ctl00_uiBodyMain_uiBodyRight_uiPerfSelector_uiBuyNowButton', by="css selector")
        if data or entry is True:
            # try:
            # sb.highlight_click("#p")
            # sb.wait_for_element_clickable(
            # f'#p > option:nth-child(2)', by="css selector").click()
            break
            # except:
            sb.highlight_click(
                "#ctl00_ctl00_uiBodyMain_uiBodyRight_uiPerfSelector_uiBuyNowButton")
            # return False
        sb.sleep(5)
        sb.refresh()


def available_data(sb):
    try:
        sb.wait_for_element_clickable(
            "#ctl00_ctl00_uiBodyMain_uiBodyRight_uiPerfSelector_uiBuyNowButton").click()
    except:
        for i in range(10):
            sb.wait_for_element_clickable("#p").click()  # here may be fault
            sb.wait_for_element_clickable(
                f'#p > option:nth-child({str(i + 1)})', by="css selector").click()
            sb.sleep(1)
            bad = sb.is_element_enabled(
                '#ctl00_ctl00_uiBodyMain_uiBodyRight_uiPerfSelector_uiPerformanceSelectorPerformance_uiSoldOutText > span > font > b', by="css selector")
            print(bad)
            if bad is False:
                sb.highlight_click(
                    "#ctl00_ctl00_uiBodyMain_uiBodyRight_uiPerfSelector_uiBuyNowButton")
                break
            elif bad is True:
                continue


def auto_choose_siting(sb, maxium_ticknumber):  # 自動輸入最佳位置
    # //*[@id="quantity--21883"]/option[1]
    sb.wait_for_element_clickable(
        "#ticketSelectorContainer > ul > li:nth-child(1) > a ", by="css selector", timeout=100000).click()
    while True:
        for i in range(2, int(maxium_ticknumber+1)):
            try:
                sb.wait_for_element('#goToPaymentButton',
                                    by="css selector", timeout=4)
                return False
            except:
                sb.highlight_click("html > body > div:nth-of-type(2) > div > div > div > div:first-of-type > div > form > div:nth-of-type(5) > div:nth-of-type(2) > div > div:first-of-type > div:nth-of-type(2) > div > div:nth-of-type(2) > section > table > tbody > tr:first-of-type > td:nth-of-type(4) > select")
                sb.highlight_click(
                    f"html > body > div:nth-of-type(2) > div > div > div > div:first-of-type > div > form > div:nth-of-type(5) > div:nth-of-type(2) > div > div:first-of-type > div:nth-of-type(2) > div > div:nth-of-type(2) > section > table > tbody > tr:first-of-type > td:nth-of-type(4) > select > option:nth-of-type({str(i)})")
                sb.highlight_click(f"#selectDeliveryType")
                sb.highlight_click(
                    f"#selectDeliveryType > option:nth-child(2)")
                sb.highlight_click(
                    f"#continueBar > div.chooseTicketsOfferDiv > button")


def action(sb):
    # token = driver.execute_script('return localStorage.getItem("reese84");')
    # 點擊進入 並且等候
    check_pagen_is_match_or_not(sb)
    available_data(sb)
    # 首頁
    # 使用最佳策略
    # ticketSelectorContainer > ul > li:nth-child(1) > a
    auto_choose_siting(sb, 5)
    # 第2頁
    sb.save_screenshot('4.png')
    sb.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sb.highlight_click('#goToPaymentButton')
    # 第3頁 loggin
    sb.save_screenshot('5.png')
    email = "ngmantsung0624@gmail.com"
    password = "abcing0193"
    sb.highlight_type("#ctl00_uiContent_Login1_tbLoginCode",
                      email, by="css selector", scroll=True)
    sb.sleep(1)
    sb.highlight_type("#ctl00_uiContent_Login1_tbPassword",
                      password, by="css selector", scroll=True)
    sb.sleep(1)
    sb.highlight_click("#ctl00_uiContent_Login1_btnLogin",
                       by="css selector", scroll=True)
    sb.sleep(1)
    try:
        sb.highlight_click(
            "#ctl00_uiContent_uiVerifyPurchase_uiAgree", by="css selector", scroll=True)
        sb.highlight_click(
            "#ctl00_uiContent_uiShowConditions_uiConditions_ctl00_uiAgree", by="css selector", scroll=True)
    except:
        pass
    sb.highlight_click("#ctl00_uiContent_uiPurchaseSubmit",
                       by="css selector", scroll=True)
    sb.sleep(10)
    typeCard, cardNumber, cardName, monthC, yearC, cvv = "master", "4966040129821234", "NG  TSUNG", 11, 2025, 123
    # otp = confirem_code.verity(cardNumber)
    if typeCard == "visa":
        sb.highlight_click(
            "#payForm > table > tbody > tr:nth-child(5) > td > div > table > tbody > tr:nth-child(5) > td > div > div > ul > li:nth-child(1) > a > img", by="css selector", scroll=True)
    elif typeCard == "master":
        sb.highlight_click(
            "#payForm > table > tbody > tr:nth-child(5) > td > div > table > tbody > tr:nth-child(5) > td > div > div > ul > li:nth-child(2) > a > img", by="css selector", scroll=True)
    elif typeCard == "AE":
        sb.highlight_click(
            "#payForm > table > tbody > tr:nth-child(5) > td > div > table > tbody > tr:nth-child(5) > td > div > div > ul > li:nth-child(3) > a > img", by="css selector", scroll=True)

    sb.highlight_type("#cardNo2", cardNumber, by="css selector", scroll=True)
    sb.sleep(1)
    sb.highlight_click("#epMonth2", by="css selector", scroll=True)
    sb.sleep(1)
    sb.highlight_click(
        f"#epMonth2 > option:nth-child({monthC + 1})", by="css selector", scroll=True)
    sb.sleep(1)
    sb.highlight_click("#epYear2", by="css selector", scroll=True)
    sb.sleep(1)
    sb.highlight_click(
        f"#epYear2 > option:nth-child({str(yearC - 2021)})", by="css selector", scroll=True)
    sb.sleep(1)
    sb.highlight_type("#cardHolder2", cardName, by="css selector", scroll=True)
    sb.sleep(1)
    sb.highlight_type(
        "#SecurityCode > td.en_text > table > tbody > tr > td:nth-child(1) > input[type=password]", cvv, by="css selector", scroll=True)
    sb.sleep(1)
    sb.highlight_click(
        "#PayInfoForm > table > tbody:nth-child(17) > tr:nth-child(2) > td > div > input:nth-child(1)", by="css selector", scroll=True)
    sb.wait_for_and_accept_alert(timeout=1000)

    sb.sleep(1000000)

    # ctl00_uiContent_uiVerifyPurchase_uiAgree
    # ctl00_uiContent_uiVerifyPurchase_uiAgree
    # ctl00_uiContent_uiShowConditions_uiConditions_ctl00_uiAgree
