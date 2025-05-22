import pytest
import sys
import os
print(sys.path)
from framework.reader import Reader
import re
from uuid import UUID
from pathlib import Path

CONFIG_PATH: str = os.getenv("CONFIG_PATH")
validation = Reader(CONFIG_PATH)


def test_general_exists():
    assert validation.config.has_section("General")


def test_watchdog_exists():
    assert validation.config.has_section("Watchdog")


@pytest.mark.parametrize("param", [
    "ScanMemoryLimit",
    "PackageType",
    "ExecArgMax",
    "AdditionalDNSLookup",
    "CoreDumps",
    "RevealSensitiveInfoInTraces",
    "ExecEnvMax",
    "MaxInotifyWatches",
    "CoreDumpsPath",
    "UseFanotify",
    "KsvlaMode",
    "MachineId",
    "StartupTraces",
    "MaxInotifyInstances",
    "Locale"
])
def test_general_params(param):
    assert validation.config.has_option("General", param), f"Параметр {param} отсутсвует в секции [General]"


@pytest.mark.parametrize("param", [
    "ConnectTimeout",
    "MaxVirtualMemory",
    "MaxMemory",
    "PingInterval"
])
def test_watchdog_params(param):
    assert validation.config.has_option("Watchdog", param), f"Параметр {param} отсутсвует в секции [Watchdog]"


def test_scan_memory_limit():
    value = int(validation.get("General", "ScanMemoryLimit"))
    assert 1024 <= value <= 8192


def test_package_type():
    value = validation.get("General", "PackageType").lower()
    assert value in {"rpm", "deb"}


def test_exec_arg_max():
    value = int(validation.get("General", "ExecArgMax"))
    assert 10 <= value <= 100


def test_additional_dns_lookup():
    value = validation.get("General", "AdditionalDNSLookup").lower()
    assert value in {"true", "false", "yes", "no"}


def test_core_dumps():
    value = validation.get("General", "CoreDumps").lower()
    assert value in {"true", "false", "yes", "no"}


def test_reveal_sensetive_info_in_traces():
    value = validation.get("General", "RevealSensitiveInfoInTraces").lower()
    assert value in {"true", "false", "yes", "no"}


def test_exec_env_max():
    value = int(validation.get("General", "ExecEnvMax"))
    assert 10 <= value <= 100


def test_max_inotify_watches():
    value = int(validation.get("General", "MaxInotifyWatches"))
    assert 1000 <= value <= 1000000


def test_core_dumps_path():
    value = validation.get("General", "CoreDumpsPath")

    path = Path(value)

    assert path.is_absolute(), f"CoreDumpsPath '{value}' не является абсолютным путем"
    assert path.exists(), f"CoreDumpsPath '{value}' не существует в системе"
    assert path.is_dir(), f"CoreDumpsPath '{value}' не является директорией"


def test_use_fanotify():
    value = validation.get("General", "UseFanotify").lower()
    assert value in {"true", "false", "yes", "no"}


def test_ksvla_mode():
    value = validation.get("General", "KsvlaMode").lower()
    assert value in {"true", "false", "yes", "no"}


def test_machine_id():
    value = validation.get("General", "MachineId")
    try:
        uuid_obj = UUID(value)
    except ValueError:
        assert False, f"MachineId '{value}' не является корректным UUID"


def test_startup_traces():
    value = validation.get("General", "StartupTraces").lower()
    assert value in {"true", "false", "yes", "no"}


def test_max_inotify_instances():
    value = int(validation.get("General", "MaxInotifyInstances"))
    assert 1024 <= value <= 8192


def test_locale():
    value = validation.get("General", "Locale").strip()

    pattern = r"^[a-zA-Z]{2,8}_[a-zA-Z]{2,8}(\.[\w\-]+)?(@[\w\-]+)?$"

    assert re.match(pattern, value)


def test_connect_timeout():
    value = validation.get("Watchdog", "ConnectTimeout")
    value_int = int(value[:-1])
    assert 1 <= value_int <= 120
    assert value[-1:] == "m"


def test_max_virtual_memory():
    value = validation.get("Watchdog", "MaxVirtualMemory")
    
    if value in {"off", "auto"}:
        assert True
    else:
        value_float = float(value)
        assert 0 < value_float <= 100


def test_max_memory():
    value = validation.get("Watchdog", "MaxMemory")
    
    if value in {"off", "auto"}:
        assert True
    else:
        value_float = float(value)
        assert 0 < value_float <= 100


def test_ping_interval():
    value = int(validation.get("Watchdog", "PingInterval"))
    assert 100 <= value <= 10000
