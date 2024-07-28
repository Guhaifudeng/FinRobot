import os
from textwrap import dedent
from typing import Annotated
from datetime import timedelta, datetime
from ..data_source import YFinanceUtils, SECUtils, FMPUtils


def combine_prompt(instruction, resource, table_str=None):
    if table_str:
        prompt = f"{table_str}\n\nResource: {resource}\n\nInstruction: {instruction}"
    else:
        prompt = f"Resource: {resource}\n\nInstruction: {instruction}"
    return prompt


def save_to_file(data: str, file_path: str):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w") as f:
        f.write(data)


class ReportAnalysisUtils:

    def analyze_income_stmt(
        ticker_symbol: Annotated[str, "ticker symbol"],
        fyear: Annotated[str, "fiscal year of the 10-K report"],
        save_path: Annotated[str, "txt file path, to which the returned instruction & resources are written."]
    ) -> str:
        """
        Retrieve the income statement for the given ticker symbol with the related section of its 10-K report.
        Then return with an instruction on how to analyze the income statement.
        """
        # chinese

        """
        获取给定股票代码的损益表及其10-K报告的相关部分。
        然后返回一份关于如何分析损益表的说明。
        """

        # Retrieve the income statement
        income_stmt = YFinanceUtils.get_income_stmt(ticker_symbol)
        df_string = "Income statement:\n" + income_stmt.to_string().strip()

        # Analysis instruction
        instruction = dedent(
            """
            Conduct a comprehensive analysis of the company's income statement for the current fiscal year. 
            Start with an overall revenue record, including Year-over-Year or Quarter-over-Quarter comparisons, 
            and break down revenue sources to identify primary contributors and trends. Examine the Cost of 
            Goods Sold for potential cost control issues. Review profit margins such as gross, operating, 
            and net profit margins to evaluate cost efficiency, operational effectiveness, and overall profitability. 
            Analyze Earnings Per Share to understand investor perspectives. Compare these metrics with historical 
            data and industry or competitor benchmarks to identify growth patterns, profitability trends, and 
            operational challenges. The output should be a strategic overview of the company’s financial health 
            in a single paragraph, less than 130 words, summarizing the previous analysis into 4-5 key points under 
            respective subheadings with specific discussion and strong data support.
            """
        )
        '''
        # 分析说明
        instruction = dedent(
            """
            对公司的本财年损益表进行全面分析。
            首先从整体收入记录入手，包括同比或环比比较，并细分收入来源以识别主要贡献者和趋势。
            检查销售成本，查找潜在的成本控制问题。
            审查毛利润率、营业利润率和净利润率，以评估成本效率、运营效益和整体盈利能力。
            分析每股收益以了解投资者的观点。
            将这些指标与历史数据和行业或竞争对手基准进行比较，以识别增长模式、盈利趋势和运营挑战。
            输出应为公司的财务健康状况的战略概述，用不到130个字的单段总结先前分析的4-5个关键点，在各自的副标题下进行具体讨论并提供强有力的数据支持。
            """
        )
        '''

        # Retrieve the related section from the 10-K report
        section_text = SECUtils.get_10k_section(ticker_symbol, fyear, 7)

        # Combine the instruction, section text, and income statement
        prompt = combine_prompt(instruction, section_text, df_string)

        save_to_file(prompt, save_path)
        return f"instruction & resources saved to {save_path}"

    def analyze_balance_sheet(
        ticker_symbol: Annotated[str, "ticker symbol"],
        fyear: Annotated[str, "fiscal year of the 10-K report"],
        save_path: Annotated[str, "txt file path, to which the returned instruction & resources are written."]
    ) -> str:
        """
        Retrieve the balance sheet for the given ticker symbol with the related section of its 10-K report.
        Then return with an instruction on how to analyze the balance sheet.
        """
        # chinese
        '''
        ```python
        """
        获取给定股票代码的资产负债表及其10-K报告的相关部分。
        然后返回一份关于如何分析资产负债表的说明。
        """
        ``` 
        '''
        balance_sheet = YFinanceUtils.get_balance_sheet(ticker_symbol)
        df_string = "Balance sheet:\n" + balance_sheet.to_string().strip()

        instruction = dedent(
            """
            Delve into a detailed scrutiny of the company's balance sheet for the most recent fiscal year, pinpointing 
            the structure of assets, liabilities, and shareholders' equity to decode the firm's financial stability and 
            operational efficiency. Focus on evaluating the liquidity through current assets versus current liabilities, 
            the solvency via long-term debt ratios, and the equity position to gauge long-term investment potential. 
            Contrast these metrics with previous years' data to highlight financial trends, improvements, or deteriorations. 
            Finalize with a strategic assessment of the company's financial leverage, asset management, and capital structure, 
            providing insights into its fiscal health and future prospects in a single paragraph. Less than 130 words.
            """
        )
        '''
        ```python
        instruction = dedent(
            """
            深入详细审查公司最近一个财年的资产负债表，明确资产、负债和股东权益的结构，以解读公司的财务稳定性和运营效率。
            重点评估通过流动资产与流动负债的流动性，通过长期债务比率的偿付能力，以及股本状况以评估长期投资潜力。
            将这些指标与前几年的数据进行对比，以突出财务趋势、改进或恶化情况。
            最后对公司的财务杠杆、资产管理和资本结构进行战略评估，在单段文字中提供对其财务健康状况和未来前景的见解。字数少于130字。
            """
        )
        ```
        '''

        section_text = SECUtils.get_10k_section(ticker_symbol, fyear, 7)
        prompt = combine_prompt(instruction, section_text, df_string)
        save_to_file(prompt, save_path)
        return f"instruction & resources saved to {save_path}"

    def analyze_cash_flow(
        ticker_symbol: Annotated[str, "ticker symbol"],
        fyear: Annotated[str, "fiscal year of the 10-K report"],
        save_path: Annotated[str, "txt file path, to which the returned instruction & resources are written."]
    ) -> str:
        """
        Retrieve the cash flow statement for the given ticker symbol with the related section of its 10-K report.
        Then return with an instruction on how to analyze the cash flow statement.
        """
        #chinese
        """
        获取给定股票代码的现金流量表及其10-K报告的相关部分。
        然后返回一份关于如何分析现金流量表的说明。
        """
        cash_flow = YFinanceUtils.get_cash_flow(ticker_symbol)
        df_string = "Cash flow statement:\n" + cash_flow.to_string().strip()

        instruction = dedent(
            """
            Dive into a comprehensive evaluation of the company's cash flow for the latest fiscal year, focusing on cash inflows 
            and outflows across operating, investing, and financing activities. Examine the operational cash flow to assess the 
            core business profitability, scrutinize investing activities for insights into capital expenditures and investments, 
            and review financing activities to understand debt, equity movements, and dividend policies. Compare these cash movements 
            to prior periods to discern trends, sustainability, and liquidity risks. Conclude with an informed analysis of the company's 
            cash management effectiveness, liquidity position, and potential for future growth or financial challenges in a single paragraph. 
            Less than 130 words.
            """
        )
        '''
                ```python
        instruction = dedent(
            """
            深入全面评估公司最近一个财年的现金流量，重点关注经营、投资和融资活动的现金流入和流出。
            检查经营活动的现金流以评估核心业务的盈利能力，仔细分析投资活动以了解资本支出和投资情况，审查融资活动以了解债务、股权变动和股息政策。
            将这些现金流动与之前的时期进行比较，以辨别趋势、可持续性和流动性风险。
            最后在单段文字中提供对公司现金管理效益、流动性状况和未来增长或财务挑战潜力的分析。字数少于130字。
            """
        )
        ```
        '''

        section_text = SECUtils.get_10k_section(ticker_symbol, fyear, 7)
        prompt = combine_prompt(instruction, section_text, df_string)
        save_to_file(prompt, save_path)
        return f"instruction & resources saved to {save_path}"

    def analyze_segment_stmt(
        ticker_symbol: Annotated[str, "ticker symbol"],
        fyear: Annotated[str, "fiscal year of the 10-K report"],
        save_path: Annotated[str, "txt file path, to which the returned instruction & resources are written."]
    ) -> str:
        """
        Retrieve the income statement and the related section of its 10-K report for the given ticker symbol.
        Then return with an instruction on how to create a segment analysis.
        """
        #chinese
        '''
        ```python
        """
        获取给定股票代码的损益表及其10-K报告的相关部分。
        然后返回一份关于如何创建细分分析的说明。
        """
        ```
        '''
        income_stmt = YFinanceUtils.get_income_stmt(ticker_symbol)
        df_string = (
            "Income statement (Segment Analysis):\n" + income_stmt.to_string().strip()
        )

        instruction = dedent(
            """
            Identify the company's business segments and create a segment analysis using the Management's Discussion and Analysis 
            and the income statement, subdivided by segment with clear headings. Address revenue and net profit with specific data, 
            and calculate the changes. Detail strategic partnerships and their impacts, including details like the companies or organizations. 
            Describe product innovations and their effects on income growth. Quantify market share and its changes, or state market position 
            and its changes. Analyze market dynamics and profit challenges, noting any effects from national policy changes. Include the cost side, 
            detailing operational costs, innovation investments, and expenses from channel expansion, etc. Support each statement with evidence, 
            keeping each segment analysis concise and under 60 words, accurately sourcing information. For each segment, consolidate the most 
            significant findings into one clear, concise paragraph, excluding less critical or vaguely described aspects to ensure clarity and 
            reliance on evidence-backed information. For each segment, the output should be one single paragraph within 150 words.
            """
        )
        '''
        ```python
        instruction = dedent(
            """
            确定公司的业务部门，并使用管理层讨论与分析（MD&A）和损益表创建细分分析，按部门划分并提供清晰的标题。
            使用具体数据说明收入和净利润，并计算变化情况。
            详细说明战略合作伙伴关系及其影响，包括公司或组织的详细信息。
            描述产品创新及其对收入增长的影响。
            量化市场份额及其变化，或说明市场地位及其变化。
            分析市场动态和利润挑战，注意国家政策变化的影响。
            包括成本方面的内容，详细说明运营成本、创新投资和渠道扩展费用等。
            支持每个陈述的证据，保持每个细分分析简明扼要，不超过60字，准确来源信息。
            对于每个细分，将最重要的发现整合成一个清晰、简明的段落，排除不太重要或描述模糊的方面，确保清晰性和基于证据的信息。
            对于每个细分，输出应为一个150字以内的段落。
            """
        )
        ```
        '''
        section_text = SECUtils.get_10k_section(ticker_symbol, fyear, 7)
        prompt = combine_prompt(instruction, section_text, df_string)
        save_to_file(prompt, save_path)
        return f"instruction & resources saved to {save_path}"

    def income_summarization(
        ticker_symbol: Annotated[str, "ticker symbol"],
        fyear: Annotated[str, "fiscal year of the 10-K report"],
        income_stmt_analysis: Annotated[str, "in-depth income statement analysis"],
        segment_analysis: Annotated[str, "in-depth segment analysis"],
        save_path: Annotated[str, "txt file path, to which the returned instruction & resources are written."]
    ) -> str:
        """
        With the income statement and segment analysis for the given ticker symbol.
        Then return with an instruction on how to synthesize these analyses into a single coherent paragraph.
        """
        # income_stmt_analysis = analyze_income_stmt(ticker_symbol)
        # segment_analysis = analyze_segment_stmt(ticker_symbol)
        #chinese
        '''
        ```python
        """
        获取给定股票代码的损益表和细分分析。
        然后返回一份关于如何将这些分析综合成一个连贯段落的说明。
        """
        ```
        '''

        instruction = dedent(
            f"""
            Income statement analysis: {income_stmt_analysis},
            Segment analysis: {segment_analysis},
            Synthesize the findings from the in-depth income statement analysis and segment analysis into a single, coherent paragraph. 
            It should be fact-based and data-driven. First, present and assess overall revenue and profit situation, noting significant 
            trends and changes. Second, examine the performance of the various business segments, with an emphasis on their revenue and 
            profit changes, revenue contributions and market dynamics. For information not covered in the first two areas, identify and 
            integrate key findings related to operation, potential risks and strategic opportunities for growth and stability into the analysis. 
            For each part, integrate historical data comparisons and provide relevant facts, metrics or data as evidence. The entire synthesis 
            should be presented as a continuous paragraph without the use of bullet points. Use subtitles and numbering for each key point. 
            The total output should be less than 160 words.
            """
        )
        '''
       ```python
        instruction = dedent(
            f"""
            损益表分析: {income_stmt_analysis},
            细分分析: {segment_analysis},
            将深入的损益表分析和细分分析的结果综合成一个连贯的段落。
            该段落应基于事实和数据驱动。
            首先，展示和评估总体收入和利润状况，注意显著的趋势和变化。
            其次，检查各业务部门的表现，重点是它们的收入和利润变化、收入贡献和市场动态。
            对于前两部分未涵盖的信息，识别并整合与运营、潜在风险以及增长和稳定的战略机会相关的关键发现。
            对每一部分，结合历史数据进行比较，并提供相关的事实、指标或数据作为证据。
            整个综合应以连续的段落形式呈现，不使用项目符号。
            对每个关键点使用副标题和编号。
            总输出应少于160字。
            """
        )
        ```
        '''

        section_text = SECUtils.get_10k_section(ticker_symbol, fyear, 7)
        prompt = combine_prompt(instruction, section_text, "")
        save_to_file(prompt, save_path)
        return f"instruction & resources saved to {save_path}"

    def get_risk_assessment(
        ticker_symbol: Annotated[str, "ticker symbol"],
        fyear: Annotated[str, "fiscal year of the 10-K report"],
        save_path: Annotated[str, "txt file path, to which the returned instruction & resources are written."]
    ) -> str:
        """
        Retrieve the risk factors for the given ticker symbol with the related section of its 10-K report.
        Then return with an instruction on how to summarize the top 3 key risks of the company.
        """
        '''
        ```python
        """
        获取给定股票代码的风险因素及其10-K报告的相关部分。
        然后返回一份关于如何总结公司前三大关键风险的说明。
        """
        ```
        '''
        company_name = YFinanceUtils.get_stock_info(ticker_symbol)["shortName"]
        risk_factors = SECUtils.get_10k_section(ticker_symbol, fyear, "1A")
        section_text = (
            "Company Name: "
            + company_name
            + "\n\n"
            + "Risk factors:\n"
            + risk_factors
            + "\n\n"
        )
        instruction = "According to the given information, summarize the top 3 key risks of the company. Less than 100 words."
        '''
        ```python
        instruction = "根据给定的信息，总结公司前三大关键风险。字数少于100字。"
        ```
        '''
        prompt = combine_prompt(instruction, section_text, "")
        save_to_file(prompt, save_path)
        return f"instruction & resources saved to {save_path}"

    def analyze_business_highlights(
        ticker_symbol: Annotated[str, "ticker symbol"],
        fyear: Annotated[str, "fiscal year of the 10-K report"],
        save_path: Annotated[str, "txt file path, to which the returned instruction & resources are written."]
    ) -> str:
        """
        Retrieve the business summary and related section of its 10-K report for the given ticker symbol.
        Then return with an instruction on how to describe the performance highlights per business of the company.
        """
        #chinese
        '''
        ```python
        """
        获取给定股票代码的业务概要及其10-K报告的相关部分。
        然后返回一份关于如何描述公司各业务表现亮点的说明。
        """
        ```
        '''
        business_summary = SECUtils.get_10k_section(ticker_symbol, fyear, 1)
        section_7 = SECUtils.get_10k_section(ticker_symbol, fyear, 7)
        section_text = (
            "Business summary:\n"
            + business_summary
            + "\n\n"
            + "Management's Discussion and Analysis of Financial Condition and Results of Operations:\n"
            + section_7
        )
        instruction = dedent(
            """
            According to the given information, describe the performance highlights per business of the company. 
            Each business description should contain one sentence of a summarization and one sentence of explanation. 
            Less than 130 words.
            """
        )
        '''
        ```python
        instruction = dedent(
            """
            根据给定的信息，描述公司各业务的表现亮点。
            每个业务描述应包含一句总结和一句解释。
            字数少于130字。
            """
        )
        ```
        '''

        prompt = combine_prompt(instruction, section_text, "")
        save_to_file(prompt, save_path)
        return f"instruction & resources saved to {save_path}"

    def analyze_company_description(
        ticker_symbol: Annotated[str, "ticker symbol"],
        fyear: Annotated[str, "fiscal year of the 10-K report"],
        save_path: Annotated[str, "txt file path, to which the returned instruction & resources are written."]
    ) -> str:
        """
        Retrieve the company description and related sections of its 10-K report for the given ticker symbol.
        Then return with an instruction on how to describe the company's industry, strengths, trends, and strategic initiatives.
        """
        #chinese
        '''
        ```python
        """
        获取给定股票代码的公司描述及其10-K报告的相关部分。
        然后返回一份关于如何描述公司的行业、优势、趋势和战略举措的说明。
        """
        ```
        '''
        company_name = YFinanceUtils.get_stock_info(ticker_symbol).get(
            "shortName", "N/A"
        )
        business_summary = SECUtils.get_10k_section(ticker_symbol, fyear, 1)
        section_7 = SECUtils.get_10k_section(ticker_symbol, fyear, 7)
        section_text = (
            "Company Name: "
            + company_name
            + "\n\n"
            + "Business summary:\n"
            + business_summary
            + "\n\n"
            + "Management's Discussion and Analysis of Financial Condition and Results of Operations:\n"
            + section_7
        )
        instruction = dedent(
            """
            According to the given information, 
            1. Briefly describe the company’s industry,
            2. Highlight core strengths and competitive advantages key products or services,
            3. Identify current industry trends, opportunities, and challenges that influence the company’s strategy,
            4. Outline recent strategic initiatives such as product launches, acquisitions, or new partnerships, and describe the company's response to market conditions. 
            Less than 400 words.
            """
        )
        '''
        ```python
        instruction = dedent(
            """
            根据给定的信息，
            1. 简要描述公司的行业，
            2. 突出核心优势和竞争优势的关键产品或服务，
            3. 确定影响公司战略的当前行业趋势、机会和挑战，
            4. 概述最近的战略举措，如产品发布、收购或新合作伙伴关系，并描述公司对市场状况的响应。
            字数少于400字。
            """
        )
        ```
        '''
        step_prompt = combine_prompt(instruction, section_text, "")
        instruction2 = "Summarize the analysis, less than 130 words."
        prompt = combine_prompt(instruction=instruction2, resource=step_prompt)
        save_to_file(prompt, save_path)
        return f"instruction & resources saved to {save_path}"

    def get_key_data(
        ticker_symbol: Annotated[str, "ticker symbol"],
        filing_date: Annotated[
            str | datetime, "the filing date of the financial report being analyzed"
        ],
    ) -> dict:
        """
        return key financial data used in annual report for the given ticker symbol and filing date
        """
        #chinese
        '''
        ```python
        """
        返回用于年度报告的给定股票代码和提交日期的关键财务数据
        """
        ```
        '''

        if not isinstance(filing_date, datetime):
            filing_date = datetime.strptime(filing_date, "%Y-%m-%d")

        # Fetch historical market data for the past 6 months
        start = (filing_date - timedelta(weeks=52)).strftime("%Y-%m-%d")
        end = filing_date.strftime("%Y-%m-%d")

        hist = YFinanceUtils.get_stock_data(ticker_symbol, start, end)

        # 获取其他相关信息
        info = YFinanceUtils.get_stock_info(ticker_symbol)
        close_price = hist["Close"].iloc[-1]

        # Calculate the average daily trading volume
        six_months_start = (filing_date - timedelta(weeks=26)).strftime("%Y-%m-%d")
        hist_last_6_months = hist[
            (hist.index >= six_months_start) & (hist.index <= end)
        ]

        # 计算这6个月的平均每日交易量
        avg_daily_volume_6m = (
            hist_last_6_months["Volume"].mean()
            if not hist_last_6_months["Volume"].empty
            else 0
        )

        fiftyTwoWeekLow = hist["High"].min()
        fiftyTwoWeekHigh = hist["Low"].max()

        # avg_daily_volume_6m = hist['Volume'].mean()

        # convert back to str for function calling
        filing_date = filing_date.strftime("%Y-%m-%d")

        # Print the result
        # print(f"Over the past 6 months, the average daily trading volume for {ticker_symbol} was: {avg_daily_volume_6m:.2f}")
        rating, _ = YFinanceUtils.get_analyst_recommendations(ticker_symbol)
        target_price = FMPUtils.get_target_price(ticker_symbol, filing_date)
        result = {
            "Rating": rating,
            "Target Price": target_price,
            f"6m avg daily vol ({info['currency']}mn)": "{:.2f}".format(
                avg_daily_volume_6m / 1e6
            ),
            f"Closing Price ({info['currency']})": "{:.2f}".format(close_price),
            f"Market Cap ({info['currency']}mn)": "{:.2f}".format(
                FMPUtils.get_historical_market_cap(ticker_symbol, filing_date) / 1e6
            ),
            f"52 Week Price Range ({info['currency']})": "{:.2f} - {:.2f}".format(
                fiftyTwoWeekLow, fiftyTwoWeekHigh
            ),
            f"BVPS ({info['currency']})": "{:.2f}".format(
                FMPUtils.get_historical_bvps(ticker_symbol, filing_date)
            ),
        }
        return result
