import sys
from configparser import ConfigParser

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <config_file_path>")
        sys.exit(1)

    config_path = sys.argv[1]

    config = ConfigParser()
    config.read(config_path)
    config_dict = {section: dict(config.items(section)) for section in config.sections()}

    #{'simulation': {'duration': '3600', 'seed': '42', 'simulation_type': '0', 'variable_scan_probability': '0'}, 'data': {'nodes': '30', 'arrival_rate': '42', 'c_scan_probability': '0.2', 'cloud_service_time': '0.8', 'edge_service_time': '0.5', 'edge_save_time': '0.1', 'response_time_qos': '3'}}

    if not config["simulation"]:
        print("Error: 'simulation' section is missing in the configuration file.")
        sys.exit(1)

    if not config["simulation"]["duration"]:
        print("Error: 'duration' parameter is missing in the 'simulation' section.")
        sys.exit(1)

    if not config["simulation"]["seed"]:
        print("Error: 'seed' parameter is missing in the 'simulation' section.")
        sys.exit(1)

    if not config["simulation"]["simulation_type"]:
        print("Error: 'simulation_type' parameter is missing in the 'simulation' section.")
        sys.exit(1)

    if not config["simulation"]["variable_scan_probability"]:
        print("Error: 'variable_scan_probability' parameter is missing in the 'simulation' section.")
        sys.exit(1)

    if not config["data"]:
        print("Error: 'data' section is missing in the configuration file.")
        sys.exit(1)

    if not config["data"]["nodes"]:
        print("Error: 'nodes' parameter is missing in the 'data' section.")
        sys.exit(1)

    if not config["data"]["arrival_rate"]:
        print("Error: 'arrival_rate' parameter is missing in the 'data' section.")
        sys.exit(1)

    if not config["data"]["c_scan_probability"]:
        print("Error: 'c_scan_probability' parameter is missing in the 'data' section.")
        sys.exit(1)

    if not config["data"]["cloud_mean_service_time"]:
        print("Error: 'cloud_mean_service_time' parameter is missing in the 'data' section.")
        sys.exit(1)

    if not config["data"]["edge_mean_service_time"]:
        print("Error: 'edge_mean_service_time' parameter is missing in the 'data' section.")
        sys.exit(1)

    if not config["data"]["edge_mean_save_time"]:
        print("Error: 'edge_mean_save_time' parameter is missing in the 'data' section.")
        sys.exit(1)






