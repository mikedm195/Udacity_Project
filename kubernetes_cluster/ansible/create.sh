ansible-playbook -i hosts kube-dependencies.yml --private-key my-new-key.pem

ansible-playbook -i hosts master.yml --private-key my-new-key.pem
ansible-playbook -i hosts workers.yml --private-key my-new-key.pem
ansible-playbook -i hosts aws-credentials.yml --private-key my-new-key.pem

ansible-playbook -i hosts jenkins-dependencies.yml --private-key my-new-key.pem