# Variables
HOST = 
PORT = 
GALAXY_ROOT = ../galaxy

start-planemo:
	@echo "Starting Planemo server on host $(HOST) and port $(PORT)"
	planemo s --host=$(HOST) --port=$(PORT) --galaxy_root=$(GALAXY_ROOT)
