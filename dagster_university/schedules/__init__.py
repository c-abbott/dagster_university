from dagster import ScheduleDefinition

from ..jobs import weekly_update_job

weekly_update_schedule = ScheduleDefinition(
    job=weekly_update_job,
    cron_schedule="0 0 * * 1",  # every Monday at midnight
)
