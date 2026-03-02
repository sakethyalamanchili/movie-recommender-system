#!/bin/bash
# Run this once after creating the repo to set up issue labels.
# Requires: gh CLI (https://cli.github.com/) authenticated.
#
# Usage:
#   chmod +x scripts/setup_labels.sh
#   ./scripts/setup_labels.sh

REPO="sakethyalamanchili/movie-recommender-system"  

echo "Setting up labels for $REPO..."

# Delete defaults (optional — uncomment if you want a clean slate)
# for label in "bug" "documentation" "duplicate" "enhancement" "good first issue" "help wanted" "invalid" "question" "wontfix"; do
#   gh label delete "$label" --repo "$REPO" --yes 2>/dev/null
# done

# Create project labels
gh label create "kafka"       --color "7B2D8B" --description "Streaming / Kafka tasks"           --repo "$REPO" --force
gh label create "ml-model"    --color "1D4ED8" --description "Model training & evaluation"       --repo "$REPO" --force
gh label create "infra"       --color "EA580C" --description "Cloud deploy, Docker, CI/CD"       --repo "$REPO" --force
gh label create "monitoring"  --color "DC2626" --description "Dashboards, alerts, SLOs"          --repo "$REPO" --force
gh label create "fairness"    --color "16A34A" --description "Fairness & bias analysis"          --repo "$REPO" --force
gh label create "bug"         --color "000000" --description "Bug fixes"                         --repo "$REPO" --force
gh label create "docs"        --color "6B7280" --description "Documentation & runbooks"          --repo "$REPO" --force
gh label create "M1"          --color "F59E0B" --description "Milestone 1"                       --repo "$REPO" --force
gh label create "M2"          --color "F59E0B" --description "Milestone 2"                       --repo "$REPO" --force
gh label create "M3"          --color "F59E0B" --description "Milestone 3"                       --repo "$REPO" --force
gh label create "M4"          --color "F59E0B" --description "Milestone 4"                       --repo "$REPO" --force
gh label create "M5"          --color "F59E0B" --description "Milestone 5"                       --repo "$REPO" --force

echo "Done! Labels created."
