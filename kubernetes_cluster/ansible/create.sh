ansible-playbook -i hosts kube-dependencies.yml --private-key my-key.pem

ansible-playbook -i hosts master.yml --private-key my-key.pem
ansible-playbook -i hosts workers.yml --private-key my-key.pem
