output "ecr_repository_url" {
  value       = module.ecr.repository_url
  description = "The URL of the ECR repository."
}

output "ecs_service_name" {
  value       = module.ecs_service.service_name
  description = "The name of the ECS service."
}
