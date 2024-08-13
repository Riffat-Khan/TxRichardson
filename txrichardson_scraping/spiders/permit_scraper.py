import scrapy

class PermitSpider(scrapy.Spider):
    name = 'permit_inspection_scraper'
    start_urls = [
        'https://discovery.cor.gov/public/permits/permitInquiry.nsf/'
    ]
    # 'DISY-D848F9', 'DISY-D848TZ',
    #'DISY-D84CFY', 'DISY-D84D2T'
    def start_requests(self):
        ids = ['DISY-D84FA5'] 
        # base_url = 'https://discovery.cor.gov/public/permits/permitInquiry.nsf/getApplicationDetails?openagent&id='
        base_url='https://www.google.com/recaptcha/api2/reload?k=6Lf3pdQjAAAAAH5h8Fczi_rKyJcBk40QFhkr45iK'
        # for id in ids:
        #     url = f"{base_url}{id}"
        #     yield scrapy.Request(
        #         url=url, 
        #         callback=self.parse
        #         )
        #base_url='https://discovery.cor.gov/public/permits/permitInquiry.nsf/index.html?OpenForm&Seq=1'
        yield scrapy.FormRequest(
                url=base_url,
                formdata={
                    '__Click': "8625866B0059D4C1.899dc6c3c55c211d862589f8005545e3/$Body/0.1FE6",
                    '%%Surrogate_appYear': "1",
                    'appYear': "24",
                    'applicationNumber': "",
                    'applicationStreetNumber': "",
                    'streetNumber': "",
                    'streetName': "",
                    '%%Surrogate_streetDirection': "1",
                    'streetDirection': "",
                    'pinNumber': "4637",
                    'action': "pin",
                    'token': "03AFcWeA6Oj8uYbx2gMk4ShzXqjc10bJ37gwXorUAceMzBajx8wIb1APho6YCnz9jB0SUO_2rvfMTDFlRKzfPEqam1dWjYvaSvAfsY751D1gNDKjWmPk-qXLXUzOQ-KDxh5cWRiPd-3O-eJjN0iODyCuv5-bFbumM2Qs6LJKabSgVhWRZMemQv3hw0ZVGDAr0zdSPxdOh6kKe9gy2fR-N2LqNLB_6KSscnIrYy8ggZHkn30z7UuSosiQr62N3kxTUL2Ei0sYk7gNCbvZ4Vx07xuuExu-QmpgJKysD9OJ7dGjbWfemJzuuX8xz2uhCkrBqgDW4sF3gbkT9cItNxxurPjNygHnCAwhw5XOKyNeQY3RDa6Z08RTP4A6yMEeuRQE5HW3Q_s9h3PFRawJRuvThZ95zHebVyi3ugtfvEVFLCrP-Hcx0mCfWX5lF-l3Dm4TMfg7870oW6NkEjMBbX5IAbCZ1oeq9cLcD8WEfwH7UMbpsPCDyilKuaS9UuJrNckY9UrECEkzCFqXuqGwDDD2jcvsp_ciKe2L1562ogIxAonOsvPu6DB569GfFxU7WTc05SWOrjOI1aHD3h_lqA6mY5e7HkNHpmCi60L0wRTvcwc1N8qXwZIlWKJ9r4Xn-KOc0kZS15euzhpE3T2zlmNsd92IMTlHMD0bBOwf-UG3V5ihJbZuxOy_fzt5BcTsP6NBbwN9zjH_0vrM7R4V-0kZAm78BvIL-Ico7JD7jFhC30MG82gd6PaC1H50TeLhercAYiUty-9h0eCa4dpAeTS6O3_gvOP1OtFwb5XQvexyydfRDpZ6qvH2PEKz9QaraI37Gt269XZm8dvc5n",
                    'error': "",
                    'returnurl': "",
                    'name': ""
                },
                method='POST',
                dont_filter=True,
                meta={'dont_redirect': False},
                callback=self.parse
            )

    def parse(self, response):
        print(response.text)
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
        
        for permit in response.css('.list-group a'):
            permit_detail_url = 'https://discovery.cor.gov/public/permits/permitInquiry.nsf/getPermitDetails?openagent&'
            permit_link = permit.attrib.get('href').split('&', 1)[1]
            if permit_link:
                full_permit_url = f"{permit_detail_url}{permit_link}"
                yield scrapy.Request(
                    url=full_permit_url, 
                    callback=self.parse_permit_details
                )
                
    def parse_permit_details(self, response):
        yield {
            'permit': response.xpath('//label[text()="Permit"]/following-sibling::div/text()').get(),
            'permit_number': response.xpath('//label[text()="Permit Number"]/following-sibling::div/text()').get(),
            'property_address': response.xpath('//label[text()="Property Address"]/following-sibling::div/text()').get(),
            'permit_type': response.xpath('//label[text()="Permit Type"]/following-sibling::div/text()').get(),
            'issue_date': response.xpath('//label[text()="Issue Date"]/following-sibling::div/text()').get(),
            'permit_status': response.xpath('//label[text()="Permit Status"]/following-sibling::div/text()').get(),
            'status_updated': response.xpath('//label[text()="Status Updated"]/following-sibling::div/text()').get(),
            'valuation': response.xpath('//label[text()="Valuation"]/following-sibling::div/text()').get(),
            'square_footage': response.xpath('//label[text()="Square Footage"]/following-sibling::div/text()').get(),
            'contractor': response.xpath('//label[text()="Contractor"]/following-sibling::div/text()').get(),
        }
        
        for inspector in response.css('.list-group a'):
            inspection_detail_url = 'https://discovery.cor.gov/public/permits/permitInquiry.nsf/getInspectionDetails?openagent&'
            inspection_link = inspector.attrib.get('href').split('&', 1)[1]
            print(inspection_link)
            if inspection_link:
                full_inspection_url = f"{inspection_detail_url}{inspection_link}"
                yield scrapy.Request(
                    url=full_inspection_url, 
                    callback=self.parse_inspection_details
                )
                
    def parse_inspection_details(self, response):
        panel_body_content = response.css('.form-horizontal').get(default='').strip()
        if panel_body_content:
            yield {
            'inspection': response.xpath('//label[text()="Inspection"]/following-sibling::div/text()').get(),
            'permit_number': response.xpath('//label[text()="Permit Number"]/following-sibling::div/text()').get(),
            'property_address': response.xpath('//label[text()="Property Address"]/following-sibling::div/text()').get(),
            'inspection_type': response.xpath('//label[text()="Inspection Type"]/following-sibling::div/text()').get(),
            'inspector': response.xpath('//label[text()="Inspector"]/following-sibling::div/text()').get(),
            'result': response.xpath('//label[text()="Result"]/following-sibling::div/text()').get(),
            'date': response.xpath('//label[text()="Date"]/following-sibling::div/text()').get(),
        }
            
