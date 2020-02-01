class employee_details:
    def __init__(self,pan,name,pakage):
        def cal_tax(self):
            if self.anual_salary<=250000:
                return 0
            elif self.anual_salary>250000 and self.anual_salary<=500000:
                return (0.05*self.anual_salary)
            elif self.anual_salary>500000 and self.anual_salary<=1000000:
                return (0.2*self.anual_salary)
            elif self.anual_salary>1000000:
                return (0.3*self.anual_salary)
        self.PANnu=pan
        self.Name=name
        self.anual_salary=pakage
        self.tax_amount=cal_tax(self)
        self.surcharge=0
        if self.anual_salary>5000000 and self.anual_salary<10000000:
            self.surcharge=(0.1*self.tax_amount)
        elif self.anual_salary>=10000000:
            self.surcharge=(0.15*self.tax_amount)
        self.cess=(0.4*self.tax_amount)
    

def main():
    employee_list=[]
    for i in range (20):
        pan=input('enter the PAN no.')
        name=input('enter the employee name')
        salary=int(input('enter anual income'))
        employee_list.append(employee_details(pan,name,salary))
    print('''pan no.            name            anual income            cess            surcharge           total income tax''')
    for i in range(20):
        print(employee_list[i].PANnu,'          ',employee_list[1].Name,'           ',employee_list[i].anual_salary,'           ',employee_list[i].cess,'           ',employee_list[i].surcharge,'          ',employee_list[i].tax_amount)
main()