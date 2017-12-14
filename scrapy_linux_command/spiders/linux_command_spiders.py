import scrapy
from scrapy_linux_command.items import SLCTitleItem
from scrapy.loader import ItemLoader
class linux_command_spiders(scrapy.spiders.Spider):
    name = 'lcs'
    allowed_domains= ["cheatography.com"]
    start_urls = ["https://www.cheatography.com/davechild/cheat-sheets/linux-command-line/"]
    def parse(self,response):
        #response.xpath('//*[@id="body_wide_shadow"]/table/tr/td/div/h3/text()').extract()处理command标题
        #response.xpath('//*[@id="body_wide_shadow"]/table/tr/td/div/div/table/tr/td/div/a/text()').extract()
        #response.xpath('//*[@id="body_wide_shadow"]/table/tr/td/div/div/table/tr/td/div/text()').extract()

        #version zero
        # SLCTitleItem.title = response.xpath('//*[@id="body_wide_shadow"]/table/tr/td/div/h3/text()').extract()
        # SLCTitleItem.content = response.xpath('//*[@id="cheat_sheet_output_table"]/tr[*]/td[*]/div/text()'
        #                                       '|//*[@id="cheat_sheet_output_table"]/tr[*]/td[*]/div/a/text()'
        #                                       '|//*[@id="cheat_sheet_output_table"]/tr[*]/td[*]/div/a/em/text()'
        #                                       '|//*[@id="cheat_sheet_output_table"]/tr[*]/td[*]/div/em/text()').extract()
        # print(SLCTitleItem.title)
        # print(SLCTitleItem.content)

        #version one
        # for sel in response.xpath('//*[@id="body_wide_shadow"]/table/tr/td/div'):
        #     slcTitle = SLCTitleItem()
        #     slcTitle['title'] = sel.xpath('h3/text()').extract()
        #     slcTitle['describe'] = sel.xpath("div/table/tr/td[@class='cheat_sheet_output_cell_2']/div/text()"
        #                                      "|div/table/tr/td[@class='cheat_sheet_output_cell_2']/div/em/text()").extract()
        #     slcTitle['content'] = sel.xpath("div/table/tr/td[@class='cheat_sheet_output_cell_1']/div/a/text()"
        #                                      "|div/table/tr/td[@class='cheat_sheet_output_cell_1']/div/a/em/text()"
        #                                     "|div/table/tr/td[@class='cheat_sheet_output_cell_1']/div/text()"
        #                                     "|div/table/tr/td[@class='cheat_sheet_output_cell_1']/div/em/text()").extract()
        #     yield slcTitle

        #version_two
        # slcTitle = ItemLoader(item = SLCTitleItem(),response=response)
        # slcTitle.add_xpath('title','//*[@id="body_wide_shadow"]/table/tr/td/div/h3/text()')
        # slcTitle.add_xpath('content',
        #                    "//*[@id='body_wide_shadow']/table/tr/td/div/div/table/tr/td[@class='cheat_sheet_output_cell_1']/div/a/text()")
        # slcTitle.add_xpath('content',
        #                    "//*[@id='body_wide_shadow']/table/tr/td/div/div/table/tr/td[@class='cheat_sheet_output_cell_1']/div/a/em/text()")
        # slcTitle.add_xpath('content',
        #                    "//*[@id='body_wide_shadow']/table/tr/td/div/div/table/tr/td[@class='cheat_sheet_output_cell_1']/div/text()")
        # slcTitle.add_xpath('content',
        #                    "//*[@id='body_wide_shadow']/table/tr/td/div/div/table/tr/td[@class='cheat_sheet_output_cell_1']/div/em/text()")
        # slcTitle.add_xpath('describe',
        #                    "//*[@id='body_wide_shadow']/table/tr/td/div/div/table/tr/td[@class='cheat_sheet_output_cell_2']/div/text()")
        # slcTitle.add_xpath('describe',
        #                    "//*[@id='body_wide_shadow']/table/tr/td/div/div/table/tr/td[@class='cheat_sheet_output_cell_2']/div/em/text()")
        # slcTitle.add_xpath('describe',
        #                    "//*[@id='body_wide_shadow']/table/tr/td/div/div/table/tr/td/div[2]/text()")
        # slcTitle.add_xpath('describe',
        #                    "//*[@id='body_wide_shadow']/table/tr/td/div/div/table/tr/td/div[2]/em/text()")
        # return slcTitle.load_item()

        # version_three
        for sel in response.xpath('//*[@id="body_wide_shadow"]/table/tr/td/div/div/table/tr'
                                  '|//*[@id="body_wide_shadow"]/table/tr/td/div'):
            slcTitle = SLCTitleItem()
            slcTitle['title'] = sel.xpath('h3/text()').extract()
            slcTitle['content'] = ' '.join(sel.xpath("td[@class='cheat_sheet_output_cell_1']/div[1]/a/text()"
                                            "|td[@class='cheat_sheet_output_cell_1']/div[1]/a/em/text()"
                                            "|td[@class='cheat_sheet_output_cell_1']/div[1]/text()"
                                            "|td[@class='cheat_sheet_output_cell_1']/div[1]/em/text()").extract())
            slcTitle['describe'] = ' '.join(sel.xpath("td[@class='cheat_sheet_output_cell_2']/div/text()"
                                             "|td[@class='cheat_sheet_output_cell_2']/div/em/text()"
                                             "|td/div[2]/text()"
                                             "|td/div[2]/em/text()").extract())
            yield slcTitle
