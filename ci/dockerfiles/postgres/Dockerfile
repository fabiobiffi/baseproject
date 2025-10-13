FROM postgres:latest

# Do NOT bake sensitive secrets into the image. Set these via an env_file or
# docker-compose environment variables at deploy time (or secrets manager).
# Recommended env vars: POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB

# Expose the default postgres port
EXPOSE 5432

# Default command is the postgres entrypoint from the base image
CMD ["postgres"]
