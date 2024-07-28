from finrobot.data_source import RedditUtils, FinnHubUtils, FMPUtils, YFinanceUtils

group_config = {
    "CIO": {
        "title": "Chief Investment Officer",
        "responsibilities": [
            "Oversee the entire investment analysis process.",
            "Integrate insights from various groups.",
            "Make the final decision on portfolio composition and adjustments.",
        ],
    },
    "groups": {
        "Market Sentiment Analysts": {
            "responsibilities": [
                "Track and interpret market trends and news.",
                "Analyze social media, news articles, and market reports for market sentiment.",
                "Provide insights on market sentiment and its potential impact on investments.",
            ],
            "with_leader": {
                "leader": {
                    "title": "Senior Market Sentiment Analyst",
                    "responsibilities": [
                        "Oversee the collection and analysis of market sentiment data.",
                        "Guide and coordinate the work of the team.",
                        "Present findings to the CIO.",
                    ],
                },
                "employees": [
                    {
                        "title": "Market Sentiment Analyst",
                        "responsibilities": [
                            "Track and interpret market trends and news.",
                            "Analyze social media and news articles for market sentiment.",
                        ],
                        "toolkits": [
                            FinnHubUtils.get_company_news,
                            RedditUtils.get_reddit_posts,
                        ],
                    },
                    {
                        "title": "Junior Market Sentiment Analyst",
                        "responsibilities": [
                            "Assist in data collection and preliminary analysis.",
                            "Support the senior analyst in preparing reports.",
                        ],
                        "toolkits": [
                            FinnHubUtils.get_company_news,
                            RedditUtils.get_reddit_posts,
                        ],
                    },
                ],
            },
            "without_leader": {
                "employees": [
                    {
                        "title": "Market Sentiment Analyst",
                        "responsibilities": [
                            "Track and interpret market trends and news.",
                            "Analyze social media and news articles for market sentiment.",
                        ],
                        "toolkits": [
                            FinnHubUtils.get_company_news,
                            RedditUtils.get_reddit_posts,
                        ],
                    },
                    {
                        "title": "Market Sentiment Analyst",
                        "responsibilities": [
                            "Conduct sentiment analysis and contribute to reports.",
                            "Collaborate with peers to ensure comprehensive coverage.",
                        ],
                    },
                    {
                        "title": "Market Sentiment Analyst",
                        "responsibilities": [
                            "Gather and process data on market sentiment.",
                            "Collaborate with peers on analysis and reporting.",
                        ],
                        "toolkits": [
                            FinnHubUtils.get_company_news,
                            RedditUtils.get_reddit_posts,
                        ],
                    },
                ]
            },
        },
        "Risk Assessment Analysts": {
            "responsibilities": [
                "Identify and quantify potential risks in the portfolio.",
                "Develop risk assessment models and tools.",
                "Monitor and report on risk exposure.",
                "Propose risk mitigation strategies.",
            ],
            "with_leader": {
                "leader": {
                    "title": "Senior Risk Analyst",
                    "responsibilities": [
                        "Oversee risk assessment and management activities.",
                        "Guide and coordinate the work of the team.",
                        "Present findings to the CIO.",
                    ],
                },
                "employees": [
                    {
                        "title": "Risk Analyst",
                        "responsibilities": [
                            "Identify and quantify potential risks in the portfolio.",
                            "Develop risk assessment models.",
                        ],
                    },
                    {
                        "title": "Junior Risk Analyst",
                        "responsibilities": [
                            "Assist in data collection and preliminary risk analysis.",
                            "Support the senior analyst in preparing reports.",
                        ],
                    },
                ],
            },
            "without_leader": {
                "employees": [
                    {
                        "title": "Risk Analyst",
                        "responsibilities": [
                            "Identify and quantify potential risks in the portfolio.",
                            "Develop risk assessment models.",
                        ],
                    },
                    {
                        "title": "Risk Analyst",
                        "responsibilities": [
                            "Conduct risk analysis and contribute to risk reports.",
                            "Collaborate with peers to ensure comprehensive risk coverage.",
                        ],
                    },
                    {
                        "title": "Risk Analyst",
                        "responsibilities": [
                            "Gather and process risk-related data.",
                            "Collaborate with peers on risk assessment and mitigation strategies.",
                        ],
                    },
                ]
            },
        },
        "Fundamental Analysts": {
            "responsibilities": [
                "Review and interpret company financial statements.",
                "Summarize key financial metrics and trends.",
                "Provide forecasts and financial health assessments.",
                "Collaborate with data scientists for deeper insights.",
            ],
            "with_leader": {
                "leader": {
                    "title": "Senior Fundamental Analyst",
                    "responsibilities": [
                        "Oversee the analysis of financial statements and annual reports.",
                        "Guide and coordinate the work of the team.",
                        "Present findings to the CIO.",
                    ],
                },
                "employees": [
                    {
                        "title": "Fundamental Analyst",
                        "responsibilities": [
                            "Review and interpret company financial statements.",
                            "Summarize key financial metrics and trends.",
                        ],
                        "toolkits": [
                            YFinanceUtils.get_stock_data,
                            FMPUtils.get_financial_metrics,
                            FMPUtils.get_historical_bvps,
                            FMPUtils.get_historical_market_cap,
                        ],
                    },
                    {
                        "title": "Junior Fundamental Analyst",
                        "responsibilities": [
                            "Assist in data collection and preliminary financial analysis.",
                            "Support the senior analyst in preparing reports.",
                        ],
                        "toolkits": [
                            YFinanceUtils.get_stock_data,
                            FMPUtils.get_financial_metrics,
                            FMPUtils.get_historical_bvps,
                            FMPUtils.get_historical_market_cap,
                        ],
                    },
                ],
            },
            "without_leader": {
                "employees": [
                    {
                        "title": "Fundamental Analyst",
                        "responsibilities": [
                            "Review and interpret company financial statements.",
                            "Summarize key financial metrics and trends.",
                            "Ask for advice from Fundamental_Analyst_2 and Fundamental_Analyst_3 when you make any conclusion.",
                            "Inspect analysis delivered by Fundamental_Analyst_2 and Fundamental_Analyst_3 and give out advices.",
                            "Reach a consensus with Fundamental_Analyst_2 and Fundamental_Analyst_3 and provide the final analysis results.",
                        ],
                        "toolkits": [
                            YFinanceUtils.get_stock_data,
                            FMPUtils.get_financial_metrics,
                            FMPUtils.get_historical_bvps,
                            FMPUtils.get_historical_market_cap,
                        ],
                    },
                    {
                        "title": "Fundamental Analyst",
                        "responsibilities": [
                            "Conduct financial analysis and contribute to reports.",
                            "Collaborate with peers to ensure thorough analysis.",
                            "Ask for advice from Fundamental_Analyst_1 and Fundamental_Analyst_3  when you make any conclusion.",
                            "Inspect analysis delivered by Fundamental_Analyst_1 and Fundamental_Analyst_3 and give out advices.",
                            "Reach a consensus with Fundamental_Analyst_1 and Fundamental_Analyst_3 and provide the final analysis results.",
                        ],
                    },
                    {
                        "title": "Fundamental Analyst",
                        "responsibilities": [
                            "Gather and process financial data.",
                            "Collaborate with peers on financial analysis and reporting.",
                            "Ask for advice from Fundamental_Analyst_1 and Fundamental_Analyst_2  when you make any conclusion.",
                            "Inspect analysis delivered by Fundamental_Analyst_1 and Fundamental_Analyst_2 and give out advices.",
                            "Reach a consensus with Fundamental_Analyst_1 and Fundamental_Analyst_2 and provide the final analysis results.",
                        ],
                        "toolkits": [
                            YFinanceUtils.get_stock_data,
                            FMPUtils.get_financial_metrics,
                            FMPUtils.get_historical_bvps,
                            FMPUtils.get_historical_market_cap,
                        ],
                    },
                ]
            },
        },
    },
}

'''
```json
{
    "CIO": {
        "title": "首席投资官",
        "responsibilities": [
            "监督整个投资分析过程。",
            "整合各小组的见解。",
            "做出投资组合构成和调整的最终决定。",
        ],
    },
    "groups": {
        "市场情绪分析师": {
            "responsibilities": [
                "跟踪和解读市场趋势和新闻。",
                "分析社交媒体、新闻文章和市场报告中的市场情绪。",
                "提供市场情绪及其对投资潜在影响的见解。",
            ],
            "with_leader": {
                "leader": {
                    "title": "高级市场情绪分析师",
                    "responsibilities": [
                        "监督市场情绪数据的收集和分析。",
                        "指导和协调团队的工作。",
                        "向首席投资官展示发现结果。",
                    ],
                },
                "employees": [
                    {
                        "title": "市场情绪分析师",
                        "responsibilities": [
                            "跟踪和解读市场趋势和新闻。",
                            "分析社交媒体和新闻文章中的市场情绪。",
                        ],
                        "toolkits": [
                            "FinnHubUtils.get_company_news",
                            "RedditUtils.get_reddit_posts",
                        ],
                    },
                    {
                        "title": "初级市场情绪分析师",
                        "responsibilities": [
                            "协助数据收集和初步分析。",
                            "支持高级分析师准备报告。",
                        ],
                        "toolkits": [
                            "FinnHubUtils.get_company_news",
                            "RedditUtils.get_reddit_posts",
                        ],
                    },
                ],
            },
            "without_leader": {
                "employees": [
                    {
                        "title": "市场情绪分析师",
                        "responsibilities": [
                            "跟踪和解读市场趋势和新闻。",
                            "分析社交媒体和新闻文章中的市场情绪。",
                        ],
                        "toolkits": [
                            "FinnHubUtils.get_company_news",
                            "RedditUtils.get_reddit_posts",
                        ],
                    },
                    {
                        "title": "市场情绪分析师",
                        "responsibilities": [
                            "进行情绪分析并撰写报告。",
                            "与同事合作确保全面覆盖。",
                        ],
                    },
                    {
                        "title": "市场情绪分析师",
                        "responsibilities": [
                            "收集和处理市场情绪数据。",
                            "与同事合作进行分析和报告。",
                        ],
                        "toolkits": [
                            "FinnHubUtils.get_company_news",
                            "RedditUtils.get_reddit_posts",
                        ],
                    },
                ]
            },
        },
        "风险评估分析师": {
            "responsibilities": [
                "识别和量化投资组合中的潜在风险。",
                "开发风险评估模型和工具。",
                "监控和报告风险暴露情况。",
                "提出风险缓解策略。",
            ],
            "with_leader": {
                "leader": {
                    "title": "高级风险分析师",
                    "responsibilities": [
                        "监督风险评估和管理活动。",
                        "指导和协调团队的工作。",
                        "向首席投资官展示发现结果。",
                    ],
                },
                "employees": [
                    {
                        "title": "风险分析师",
                        "responsibilities": [
                            "识别和量化投资组合中的潜在风险。",
                            "开发风险评估模型。",
                        ],
                    },
                    {
                        "title": "初级风险分析师",
                        "responsibilities": [
                            "协助数据收集和初步风险分析。",
                            "支持高级分析师准备报告。",
                        ],
                    },
                ],
            },
            "without_leader": {
                "employees": [
                    {
                        "title": "风险分析师",
                        "responsibilities": [
                            "识别和量化投资组合中的潜在风险。",
                            "开发风险评估模型。",
                        ],
                    },
                    {
                        "title": "风险分析师",
                        "responsibilities": [
                            "进行风险分析并撰写风险报告。",
                            "与同事合作确保全面覆盖。",
                        ],
                    },
                    {
                        "title": "风险分析师",
                        "responsibilities": [
                            "收集和处理风险相关数据。",
                            "与同事合作进行风险评估和缓解策略。",
                        ],
                    },
                ]
            },
        },
        "基本面分析师": {
            "responsibilities": [
                "审查和解读公司财务报表。",
                "总结关键财务指标和趋势。",
                "提供预测和财务健康评估。",
                "与数据科学家合作获取更深入的见解。",
            ],
            "with_leader": {
                "leader": {
                    "title": "高级基本面分析师",
                    "responsibilities": [
                        "监督财务报表和年度报告的分析。",
                        "指导和协调团队的工作。",
                        "向首席投资官展示发现结果。",
                    ],
                },
                "employees": [
                    {
                        "title": "基本面分析师",
                        "responsibilities": [
                            "审查和解读公司财务报表。",
                            "总结关键财务指标和趋势。",
                        ],
                        "toolkits": [
                            "YFinanceUtils.get_stock_data",
                            "FMPUtils.get_financial_metrics",
                            "FMPUtils.get_historical_bvps",
                            "FMPUtils.get_historical_market_cap",
                        ],
                    },
                    {
                        "title": "初级基本面分析师",
                        "responsibilities": [
                            "协助数据收集和初步财务分析。",
                            "支持高级分析师准备报告。",
                        ],
                        "toolkits": [
                            "YFinanceUtils.get_stock_data",
                            "FMPUtils.get_financial_metrics",
                            "FMPUtils.get_historical_bvps",
                            "FMPUtils.get_historical_market_cap",
                        ],
                    },
                ],
            },
            "without_leader": {
                "employees": [
                    {
                        "title": "基本面分析师",
                        "responsibilities": [
                            "审查和解读公司财务报表。",
                            "总结关键财务指标和趋势。",
                            "在得出任何结论时，向基本面分析师2和基本面分析师3请教。",
                            "检查基本面分析师2和基本面分析师3提交的分析，并提出建议。",
                            "与基本面分析师2和基本面分析师3达成共识，并提供最终分析结果。",
                        ],
                        "toolkits": [
                            "YFinanceUtils.get_stock_data",
                            "FMPUtils.get_financial_metrics",
                            "FMPUtils.get_historical_bvps",
                            "FMPUtils.get_historical_market_cap",
                        ],
                    },
                    {
                        "title": "基本面分析师",
                        "responsibilities": [
                            "进行财务分析并撰写报告。",
                            "与同事合作确保全面分析。",
                            "在得出任何结论时，向基本面分析师1和基本面分析师3请教。",
                            "检查基本面分析师1和基本面分析师3提交的分析，并提出建议。",
                            "与基本面分析师1和基本面分析师3达成共识，并提供最终分析结果。",
                        ],
                    },
                    {
                        "title": "基本面分析师",
                        "responsibilities": [
                            "收集和处理财务数据。",
                            "与同事合作进行财务分析和报告。",
                            "在得出任何结论时，向基本面分析师1和基本面分析师2请教。",
                            "检查基本面分析师1和基本面分析师2提交的分析，并提出建议。",
                            "与基本面分析师1和基本面分析师2达成共识，并提供最终分析结果。",
                        ],
                        "toolkits": [
                            "YFinanceUtils.get_stock_data",
                            "FMPUtils.get_financial_metrics",
                            "FMPUtils.get_historical_bvps",
                            "FMPUtils.get_historical_market_cap",
                        ],
                    },
                ]
            },
        },
    },
}
```

'''