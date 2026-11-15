"""
    Download the Spark Kafka connector and its dependencies into jars (once)
"""
import urllib.request
from pathlib import Path

MAVEN = "https://repo1.maven.org/maven2"
JARS = [("org.apache.spark", "spark-sql-kafka-0-10_2.13", "4.3.0"), 
    ("org.apache.spark", "spark-token-provider-kafka-0-10_2.13", "4.3.0"),
    ("org.apache.kafka", "kafka-clients", "3.9.2"),
    ("org.apache.commons", "commons-pool2", "2.13.1"),
]
folder = Path.cwd() / "jars"
folder.mkdir(exist_ok=True)
print(folder)
for group, artifact, version in JARS:
    name = f"{artifact}-{version}.jar"
    url = f"{MAVEN}/{group.replace('.', '/')}/{artifact}/{version}/{name}"
    print(f"url: {url}")
    if not (folder / name).exists():
        urllib.request.urlretrieve(url, folder / name)
    print(f"{name}: {(folder / name).stat().st_size // 1024} KB")