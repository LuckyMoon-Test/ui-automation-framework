# UI 自动化测试框架 (UI Automation Framework)

> **声明 (Disclaimer)**：
> 1. 本项目为个人 UI 自动化测试学习与练习项目，**不包含任何被测试系统（黑马头条）的源代码**。
> 2. 项目中的所有代码均用于展示自动化测试框架的搭建思路（PO 模式、单例模式、数据驱动、CI/CD 等）。
> 3. 测试对象仅指向公开的测试练习环境，无任何商业或侵权意图。

## 项目简介
本项目是一个基于 **Python + Selenium + Appium + Pytest** 的 UI 自动化测试框架。主要用于学习并实践企业级 Web 端与 App 端的自动化测试。

项目严格遵循 **PO (Page Object) 设计模式**，实现了测试数据、业务逻辑与底层操作的彻底解耦。同时集成了 **GitHub Actions 持续集成 (CI)**，具备在云端自动部署环境并执行测试的能力。

## 技术栈
- **语言**：Python 3.11
- **Web 自动化**：Selenium 4
- **App 自动化**：Appium-Python-Client
- **测试框架**：Pytest
- **数据驱动**：YAML
- **测试报告**：Allure
- **CI/CD**：GitHub Actions

## 目录结构
```text
├── .github/workflows/    # GitHub Actions 持续集成配置文件 (ci.yml)
├── uiAutoTestHmtt/       # 测试项目主目录
│   ├── base/             # 底层封装 (Base层，WebBase, AppBase)
│   ├── data/             # 测试数据 (YAML文件)
│   ├── page/             # 页面对象层 (PO模式，元素定位与业务逻辑分离)
│   ├── scripts/          # 测试用例层 (Test层，编写断言)
│   ├── tools/            # 公共工具类 (单例模式 Driver管理、日志、YAML读取)
│   └── config.py         # 全局路径配置
├── requirements.txt      # 项目依赖清单
└── pytest.ini            # Pytest 运行配置
