# Crono API Client

	$ pip install crono_api_client
	$ python
	>>> import crono_api_client as crono
	>>> crono.request('POST', https://your.app/').after(hours=42)

## How to

Get all jobs

```python
job_uuids = crono.jobs()
```

Get a job

```python
job_json = crono.job(<string:job_uuid>)
```

Schedule a job

```python
job_uuid = crono.<task>(<args>, <kwargs>).<trigger>(<args>, <kwargs>)
# or
job_uuid = crono.<trigger>(<args>, <kwargs>).<task>(<args>, <kwargs>)
```

Delete a job

```python
job_uuid = crono.delete(<string:job_uuid>)
```

## Development

Packaging

	# Generating distribution archives
	python setup.py sdist bdist_wheel

	# Uploading the distribution archives
	twine upload --skip-existing dist/*
