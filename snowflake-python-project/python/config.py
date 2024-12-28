import os

SNOWFLAKE_CONFIG = {
    'user': os.getenv('mrajamani'),
    'password': os.getenv('Muruga@20608'),
    'account': os.getenv('POC_ITIM'),
    'database': os.getenv('POC_CICD_PY'),
    'warehouse': os.getenv('POC_ITIM_PERIASAMY'),
}
