import scrapy
import os
from dotenv import load_dotenv
from twocaptcha import TwoCaptcha
from urllib.parse import urlparse, parse_qs

load_dotenv()

class PermitSpider(scrapy.Spider):
    name = 'permit_inspection_scraper'
    start_urls = [
        'https://discovery.cor.gov/public/permits/permitInquiry.nsf/'
    ]
    
    def __init__(self, *args, **kwargs):
        super(PermitSpider, self).__init__(*args, **kwargs)
        self.api_key = os.getenv('APIKEY_2CAPTCHA', '3ce3d404b09722a1292a68236c82e319')
        self.solver = TwoCaptcha(self.api_key)
    
    # 6Lf3pdQjAAAAAH5h8Fczi_rKyJcBk40QFhkr45iK
    
    def start_requests(self):
        # yield scrapy.Request(url=base_url, callback=self.parse_form)
        ids = ['DISY-D84FA5'] 
        # base_url = 'https://discovery.cor.gov/public/permits/permitInquiry.nsf/getApplicationDetails?openagent&id='
        # base_url='https://discovery.cor.gov/public/permits/permitInquiry.nsf/index.html'
        # headers = {
        #     'x-client-data': 'CI22yQEIprbJAQipncoBCNnuygEIlaHLAQiHoM0BCI2nzQEIra7OAQjrus4B'
        # }
        
        # for id in ids:
        #     url = f"{base_url}{id}"
        #     yield scrapy.Request(
        #         url=url, 
        #         callback=self.parse
        #         )
        base_url='https://discovery.cor.gov/public/permits/permitInquiry.nsf/index.html?OpenForm&Seq=1'
          
        captcha_url = 'https://discovery.cor.gov/public/permits/permitInquiry.nsf/index.html'
        # solver = TwoCaptcha('3ce3d404b09722a1292a68236c82e319')
        # site_key = '03AFcWeA7p30C3XxzvqzA1J5nweEf9ZxqkxewvP9EffK09BMKpsoUKv31jHS5g09yyhhRz5zha2YODa0kL3gIJNITjc_nvWDDeZmirRCQWOAl7LzuZpAhUt1SIO4WYSiQXLUdD7-thalfRr-xuZ848iNJeeLaaLdiEI1gcA48OUeDnzoWLF3iesEc4DHyQYXN29urzYjKoZrQdWaqe1YlZynoRtR6poQpG3wZM-UNe_OxK43duwyrVWutInRDpatWp0YbxpvLqt7UfAFKpH7wAxUFjN9GWSTD7e74CiW7MaRbdT3th-nxFc3URmnGRvbQPbvyKvfQQjz2SLzDjY8ywEoDSH2E_a3mE-3E-hX4yQOatMm1Jqtbx85DC6oIejeh5AkDCfN6v5geqh9kg95ZInT5OrngGYHsko8bOTHz9K1imJXTDY7bnivvxiDXgqcrq4j_JddHD1FB-Tv8PL-p9bMsiFc7lKJG-Fu631HHJUQgplGX3Ved9MxjhPrSXo0B1N690D5ULOfnW4qH9VklvzrcGtJHvLV3n3CRnidShdB3xCnlCD4vbzDGE1_r6TdEqFIfgthXT7iYfdU7VVgcV4WPwS22C9CvLb0BlNzx4ZnRsrVEc66GsaZJdP1y4vVUJjJADQVSAOWj5FtVu_vCgSNCmUn2mEXGNhfN5cV8aXfj-evUMxYD1Ai1Bfq-uu2oJU-hxhOQulX2E-vbAjz8wGvTQoy_X-bxWtTteLrfLqVulv-wRXcp7nbugG9B5Z8wP20B8n6gWLpNorlZUAgJKFzlc8oc3UpZx8SaOMeQnSm9ffsiIm3-SwwWBAU9ilGTR-eUs3tnHQ0kpLD5JSOJWi4rtKIHkgyPoQxTI8SikYvYf7bI767F_N-CKYMWH3OLoyK_ivQlT7oS0aNE4qT6RHovEC21eNMCe_WIzcVtjHOjac99KN-YLP87_H3XjJa6sjpqyHQnwsU5WHGdJ8qQfmNk2CatsU-19V4vuzs70w_69euzxs6_ty4hCKb5EQAwBLSclC9KCvzYbUt6mPxDZVCAOr1ZYI4bjcuZ4M1ghuxVAuCw8x55r6gctaS0iHfUmA7lv9sgtK9vE4zkbfnBMa-QMUzrSCzGd0tSwv9ui-1Yfo1aW4188ouGDeKfgfjdC5_quW9JjKWWrmyCIPJyYlHWaa9yKLWkOzCUbOJRULZDNSdF0FZi-22RXyKQOpSxqk9GmwDe5YJU1wPiZNDMwmeXgPROgxC-12WDBsOSPtdLNvHQGTlxiVsIyChQkS3kWwbZfhwZWS1ziHLnGWsanJ2BrproN3Uv94oXQG29URcxHsK3M81O6UBh-PIcxaE6FsxEMuU-pT9iIA3cXLwnloLP4aaf6rsuVVQhj5hKPP1OVOlaOUGk85-38dDzhm2sxc_XXBe5EKeLCjlj4h2hvjvuYgaJoJxk8lLODfkktFTw2P-jlHwTCZaLok94aylybTmqTgQsl2MAQOuK88lnfmGcXlaRhfnOca3DPHlS4PNfnHzfeaRersgB7ahTy5L8VHCXaCZwUPfSmM_cUio3vK3X5L092iM8tjdDymo6bRopHPORteyiXHkHVOWxQbP1NkaUwOopABH804-0lPpajv7W-qkuM8dZP3oEPufnj6sTcwZKNpLn1Eko'
        site_key = '6Lf3pdQjAAAAAH5h8Fczi_rKyJcBk40QFhkr45iK'
        print('+++++++++++++++++++++++++++',self.solver.API_KEY)
        result = self.solver.recaptcha(
        sitekey=site_key, 
        url=captcha_url,
        version='v3',
        )
        recaptcha_token = result.get('code')
        print('code:::::::::::::::::::::::::::::', recaptcha_token)
        
        yield scrapy.FormRequest(
                url=base_url,
                formdata={
                    '__Click': "8625866B0059D4C1.899dc6c3c55c211d862589f8005545e3/$Body/0.1FE6",
                    'Surrogate_appYear': "1",
                    'appYear': "24",
                    'applicationNumber': "",
                    'applicationStreetNumber': "",
                    'streetNumber': "",
                    'streetName': "",
                    'Surrogate_streetDirection': "1",
                    'streetDirection': "",
                    'pinNumber': "5465",
                    'action': "pin",
                    'token': recaptcha_token,
                    'error': "",
                    'returnurl': "",
                    'name': ""
                },
                method='POST',
                dont_filter=True,
                meta={'handle_httpstatus_all': True, 'dont_redirect': True},
                callback=self.parse
            )

    def parse(self, response):
        # headers = response.headers
        print(response.url)
    
        
        # yield {
        #     'year': response.xpath('//label[text()="Year"]/following-sibling::div/text()').get(),
        #     'number': response.xpath('//label[text()="Number"]/following-sibling::div/text()').get(),
        #     'address': response.xpath('//label[text()="Address"]/following-sibling::div/text()').get(),
        #     'tenant_number': response.xpath('//label[text()="Tenant Number"]/following-sibling::div/text()').get(),
        #     'tenant_name': response.xpath('//label[text()="Tenant Name"]/following-sibling::div/text()').get(),
        #     'type': response.xpath('//label[text()="Type"]/following-sibling::div/text()').get(),
        #     'status': response.xpath('//label[text()="Status"]/following-sibling::div/text()').get(),
        #     'date': response.xpath('//label[text()="Date"]/following-sibling::div/text()').get(),
        # }
        
        # for permit in response.css('.list-group a'):
        #     permit_detail_url = 'https://discovery.cor.gov/public/permits/permitInquiry.nsf/getPermitDetails?openagent&'
        #     permit_link = permit.attrib.get('href').split('&', 1)[1]
        #     if permit_link:
        #         full_permit_url = f"{permit_detail_url}{permit_link}"
        #         yield scrapy.Request(
        #             url=full_permit_url, 
        #             callback=self.parse_permit_details
        #         )
                
    # def parse_permit_details(self, response):
    #     yield {
    #         'permit': response.xpath('//label[text()="Permit"]/following-sibling::div/text()').get(),
    #         'permit_number': response.xpath('//label[text()="Permit Number"]/following-sibling::div/text()').get(),
    #         'property_address': response.xpath('//label[text()="Property Address"]/following-sibling::div/text()').get(),
    #         'permit_type': response.xpath('//label[text()="Permit Type"]/following-sibling::div/text()').get(),
    #         'issue_date': response.xpath('//label[text()="Issue Date"]/following-sibling::div/text()').get(),
    #         'permit_status': response.xpath('//label[text()="Permit Status"]/following-sibling::div/text()').get(),
    #         'status_updated': response.xpath('//label[text()="Status Updated"]/following-sibling::div/text()').get(),
    #         'valuation': response.xpath('//label[text()="Valuation"]/following-sibling::div/text()').get(),
    #         'square_footage': response.xpath('//label[text()="Square Footage"]/following-sibling::div/text()').get(),
    #         'contractor': response.xpath('//label[text()="Contractor"]/following-sibling::div/text()').get(),
    #     }
        
    #     for inspector in response.css('.list-group a'):
    #         inspection_detail_url = 'https://discovery.cor.gov/public/permits/permitInquiry.nsf/getInspectionDetails?openagent&'
    #         inspection_link = inspector.attrib.get('href').split('&', 1)[1]
    #         print(inspection_link)
    #         if inspection_link:
    #             full_inspection_url = f"{inspection_detail_url}{inspection_link}"
    #             yield scrapy.Request(
    #                 url=full_inspection_url, 
    #                 callback=self.parse_inspection_details
    #             )
                
    # def parse_inspection_details(self, response):
    #     panel_body_content = response.css('.form-horizontal').get(default='').strip()
    #     if panel_body_content:
    #         yield {
    #         'inspection': response.xpath('//label[text()="Inspection"]/following-sibling::div/text()').get(),
    #         'permit_number': response.xpath('//label[text()="Permit Number"]/following-sibling::div/text()').get(),
    #         'property_address': response.xpath('//label[text()="Property Address"]/following-sibling::div/text()').get(),
    #         'inspection_type': response.xpath('//label[text()="Inspection Type"]/following-sibling::div/text()').get(),
    #         'inspector': response.xpath('//label[text()="Inspector"]/following-sibling::div/text()').get(),
    #         'result': response.xpath('//label[text()="Result"]/following-sibling::div/text()').get(),
    #         'date': response.xpath('//label[text()="Date"]/following-sibling::div/text()').get(),
    #     }
            
