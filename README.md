# Python Logging Template

This repository contains a Python logging template. It is designed to provide a flexible and configurable logging setup for your Python applications.

## Contents

The main components of this template are:

- `logger_config.py`: This Python file contains the definitions for `SensitiveDataFilter` and `PasswordFilter`, which are custom filters used to sanitize sensitive data from the logs.

- `logging_config.yaml`: This YAML file is a configuration file for the logging system. It defines the loggers, handlers, filters, and formatters that will be used in the application.

- `logging_config/*.yaml`: Ready to use logging configs in YAML format.

## Usage

To use this logging template, import the logger configuration in your Python script and use it to configure the Python `logging` module. The `logging_config.yaml` file can be modified to customize the logging setup according to your needs.

## Features

- **Sensitive Data Filter**: This filter removes sensitive data from the logs to ensure that it is not accidentally exposed.

- **Password Filter**: This filter removes password information from the logs for security purposes.

## Multi-thread/process
The `queue_handler` is used in logging to manage log messages in a multi-threaded or multi-process environment. It places log messages into a queue, which a separate thread or process reads from, ensuring that logging operations do not block the main execution flow of your application. 

### Is it Necessary?

- **Multi-threaded/Multi-process Applications**: Essential for handling log messages efficiently.
- **Single-threaded Applications**: Not necessary, but it can still be useful for organizing and managing log messages.

If your application involves concurrent execution, using a `queue_handler` is beneficial for robust and efficient logging. If it's a simple, single-threaded application, it might not be necessary.
