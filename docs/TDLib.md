# TDLip

[Documentation]([TDLib](https://core.telegram.org/tdlib))

## What is TDLip?

TDLib (Telegram Database Library) is a cross-platform, fully functional Telegram client. We designed it to help third-party developers create their own `custom apps` using the Telegram platform.

[Read about TDLib on the Telegram blog >](https://telegram.org/blog/tdlib)

## [TDLib Advantages](https://core.telegram.org/tdlib#tdlib-advantages)
* **Cross-platform**. TDLib can be used on Android, iOS, Windows, macOS, Linux, WebAssembly, FreeBSD, Windows Phone, watchOS, tvOS, Tizen, Cygwin. It should also work on other *nix systems with or without minimal effort.

* **Multilanguage**. TDLib can be easily used with any programming language that is able to execute C functions. Additionally it already has native bindings to Java (using JNI) and C# (using C++/CLI).

* **Easy to use**. TDLib takes care of all network implementation details, encryption and local data storage.

* **High-performance**. In the Telegram Bot API, each TDLib instance handles more than 24,000 active bots simultaneously.
* **Well-documented**. All TDLib API methods and public interfaces are [fully documented](https://core.telegram.org/tdlib/docs/).

* **Consistent**. TDLib guarantees that all updates will be delivered in the right order.
Reliable. TDLib remains stable on slow and unreliable Internet connections.
Secure: All local data is encrypted using a user-provided encryption key.
Fully-asynchronous. Requests to TDLib don't block each other or anything else, responses will be sent when they are available.


## Where can I use this TDLib?
The TDLib (Telegram Database Library) is not related to databases, but rather it stands for "Telegram Database Library." It's a software library developed by Telegram to provide a high-level API for building Telegram clients.

TDLib is used by developers to create custom Telegram clients with more advanced features than the standard Telegram app. These clients can be used on various platforms including desktop, mobile, and web. TDLib abstracts many of the complex details of working with the Telegram API, allowing developers to focus on creating user interfaces and implementing specific functionalities.

Here are some places where you can use TDLib:

1. **Custom Telegram Clients:** TDLib is mainly used to create custom Telegram clients with unique features or user interfaces. Developers can build clients that suit specific needs, integrate additional features, or provide alternative user experiences.

2. **Third-Party Apps:** Independent developers and companies can use TDLib to develop third-party Telegram clients that provide distinct features not found in the official Telegram apps.

3. **Messaging Bots:** TDLib can also be used to create advanced messaging bots that interact with users on the Telegram platform, responding to messages, handling user commands, and performing various actions.

4. **Automation Tools:** Developers can leverage TDLib to build automation tools that interact with Telegram, such as sending messages, managing groups, or extracting information from conversations.

5. **Integrations:** TDLib can be integrated into other applications or services, enabling communication via Telegram within those contexts.

To use TDLib, you would typically integrate the library into your application's codebase and use its API to handle various Telegram-related tasks. Keep in mind that TDLib is more suitable for developers who are familiar with programming and software development, as it involves working with APIs, data structures, and user interfaces.

It's important to stay updated with the latest documentation and releases for TDLib, as Telegram may make updates and improvements to the library over time. You can find more information about TDLib and its documentation on Telegram's official GitHub repository or developer resources.