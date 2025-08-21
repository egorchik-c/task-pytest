# Руководство по сборке проекта

Данный проект является практическим заданием к отбору на направление Python 2025 

### Используемое ПО 
- pytest
- python (версия не ниже 3.6)
- docker
- virtualenv

## Запуск проекта (docker)

Перед запуском тестов подразумивается наличие Docker, docker-compose и выполнения следующих команд в терминале Linux в нужной директории.
Для запуска проекта требуется выполнение следущих команд:
```
docker-compose up --build
```

## Настройка окружения и запуск проекта (без docker)

Перед запуском тестов подразумивается наличие Python и выполнения следующих команд в терминале Linux в нужной директории.
Для создания виртуального окружения:
```
pip install virtualenv
virtualenv -p python[Версия питона] venv
```
Запуск виртуального окружения
```
# Активация venv
source venv/bin/activate 

# Выполнение в venv
pip install -r requirements.txt

# Запуск Тестов (в venv!)
pytest 

# Деактивация venv
deactivate
```

# Описание автотестов

| Название теста | Что проверяет |
|:----------------|:--------------|
| test_general_exists | Секция `[General]` существует |
| test_watchdog_exists | Секция `[Watchdog]` существует |
| test_general_params | Все обязательные параметры в секции `[General]` присутствуют |
| test_watchdog_params | Все обязательные параметры в секции `[Watchdog]` присутствуют |
| test_scan_memory_limit | Значение `ScanMemoryLimit` в диапазоне [1024, 8192] |
| test_package_type | `PackageType` — "rpm" или "deb" |
| test_exec_arg_max | Значение `ExecArgMax` в диапазоне [10, 100] |
| test_additional_dns_lookup | `AdditionalDNSLookup` — одно из: "true", "false", "yes", "no" |
| test_core_dumps | `CoreDumps` — одно из: "true", "false", "yes", "no" |
| test_reveal_sensetive_info_in_traces | `RevealSensitiveInfoInTraces` — одно из: "true", "false", "yes", "no" |
| test_exec_env_max | Значение `ExecEnvMax` в диапазоне [10, 100] |
| test_max_inotify_watches | Значение `MaxInotifyWatches` в диапазоне [1000, 1000000] |
| test_core_dumps_path | `CoreDumpsPath` — абсолютный путь, существует и является директорией |
| test_use_fanotify | `UseFanotify` — одно из: "true", "false", "yes", "no" |
| test_ksvla_mode | `KsvlaMode` — одно из: "true", "false", "yes", "no" |
| test_machine_id | `MachineId` — корректный UUID |
| test_startup_traces | `StartupTraces` — одно из: "true", "false", "yes", "no" |
| test_max_inotify_instances | Значение `MaxInotifyInstances` в диапазоне [1024, 8192] |
| test_locale | `Locale` соответствует формату языка и страны (RFC 3066) |
| test_connect_timeout | `ConnectTimeout` — целое число [1, 120] + символ "m" |
| test_max_virtual_memory | `MaxVirtualMemory` — "off", "auto" или число (0, 100] |
| test_max_memory | `MaxMemory` — "off", "auto" или число (0, 100] |
| test_ping_interval | Значение `PingInterval` в диапазоне [100, 10000] |

## P.S
### Проект выполнялся с использованием следующих средств
- Ubuntu 24.04.2
- Python 3.12.3
- pip 24.0
- Docker 28.0.4
- virtualenv 20.25.0
- pytest 8.3.5

