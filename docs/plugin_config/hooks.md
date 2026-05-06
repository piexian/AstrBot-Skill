# 插件事件钩子

插件事件钩子使用 `astrbot.api.event.filter` 下的 `@filter.on_*` 或
`@filter.after_message_sent()` 装饰器注册。钩子处理函数必须使用 `async def`。

> 事件钩子不要和 `@filter.command`、`@filter.command_group`、
> `@filter.event_message_type`、`@filter.platform_adapter_type`、
> `@filter.permission_type` 叠加使用。

## 常用钩子

| 钩子 | 触发时机 | 典型用途 |
| --- | --- | --- |
| `@filter.on_astrbot_loaded()` | AstrBot 初始化完成后 | 启动后台任务、预热缓存 |
| `@filter.on_waiting_llm_request()` | 准备调用 LLM、等待会话锁前 | 发送等待提示、记录排队状态 |
| `@filter.on_llm_request()` | 调用 LLM 前 | 修改 `ProviderRequest`、追加 system prompt |
| `@filter.on_llm_response()` | LLM 返回后 | 检查或调整 `LLMResponse` |
| `@filter.on_using_llm_tool()` | LLM 工具调用前 | 记录工具调用、校验参数 |
| `@filter.on_llm_tool_respond()` | LLM 工具返回后 | 记录工具结果、做后处理 |
| `@filter.on_decorating_result()` | 消息结果发送前 | 修改 `event.get_result().chain` |
| `@filter.after_message_sent()` | 消息发送到平台后 | 记录发送结果、清理临时状态 |

## 示例

```python
from astrbot.api.event import AstrMessageEvent, filter
from astrbot.api.provider import LLMResponse, ProviderRequest


@filter.on_llm_request()
async def on_llm_request(self, event: AstrMessageEvent, req: ProviderRequest) -> None:
    req.system_prompt += "\n请优先使用简洁中文回答。"


@filter.on_llm_response()
async def on_llm_response(self, event: AstrMessageEvent, resp: LLMResponse) -> None:
    print(resp)


@filter.after_message_sent()
async def after_message_sent(self, event: AstrMessageEvent) -> None:
    print("message sent")
```

## 注意事项

- 钩子里通常不要 `yield event.plain_result(...)`。需要主动发送消息时，使用
  `await event.send(...)`。
- `on_decorating_result` 适合修改当前事件已有的回复结果，例如追加消息链组件。
- Agent Runner 的 `BaseAgentRunHooks` 是另一层机制，见 `agent/agent-related-hooks.md`。
