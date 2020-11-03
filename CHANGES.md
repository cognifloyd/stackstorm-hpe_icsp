# Change Log

# 0.7.0

- Converted the following workflows to Orquesta:
    - `hpe_icsp.icsp_ids_to_os`
    - `hpe_icsp.icsp_multi_server_attribute_add`
  Contributed by Nick Maludy (Encore Technologies)

- Added the following actions/workflows to faciliate the conversion above:
    - `hpe_icsp.icsp_id_to_os`: Maps a single ID to an OS
    - `hpe_icsp.icsp_single_server_attribute_add`: Adds an attribute to a single server.

# 0.6.4

- Minor linting fix

# 0.6.3

- Minor linting fix

# 0.6.1

- Addition of of get servers action to list current registered servers
- Update to delete server action to take three types of identifier

# 0.6.0

- Updated action `runner_type` from `run-python` to `python-script`

# 0.5.0

- Rename `config.yaml` to `config.schema.yaml` and update to use schema.

# 0.4.0

- Rename pack from hpe-icsp to hpe_icsp
