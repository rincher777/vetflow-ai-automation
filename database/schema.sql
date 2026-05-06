-- Estrutura de Banco de Dados para o VetFlow AI
-- Focado em integridade de estoque e agendamentos médicos

-- 1. Tabela de Insumos (Baseado na expertise MedStock)
CREATE TABLE inventory (
    id SERIAL PRIMARY KEY,
    sku VARCHAR(50) UNIQUE NOT NULL,      -- Código único (ex: VAC-V10-001)
    name VARCHAR(100) NOT NULL,           -- Nome do insumo ou medicamento
    description TEXT,
    quantity_stock INTEGER DEFAULT 0,     -- Saldo atual
    min_quantity INTEGER DEFAULT 5,       -- Alerta de estoque baixo
    unit_price DECIMAL(10, 2),            -- Valor para cálculo de custo/procedimento
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. Tabela de Agendamentos (Onde a IA insere os dados)
CREATE TABLE appointments (
    id SERIAL PRIMARY KEY,
    pet_name VARCHAR(100) NOT NULL,
    owner_name VARCHAR(100),
    owner_phone VARCHAR(20),              -- Para integração futura com bot de WhatsApp
    service_type VARCHAR(50) NOT NULL,    -- Ex: Vacinação V10, Consulta Geral
    appointment_date TIMESTAMP NOT NULL,
    status VARCHAR(20) DEFAULT 'pending', -- pending, confirmed, completed, cancelled
    
    -- Chave estrangeira: Vincula o agendamento ao insumo que será consumido
    inventory_id INTEGER REFERENCES inventory(id),
    
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 3. Inserção de dados iniciais para teste (Seeds)
INSERT INTO inventory (sku, name, quantity_stock, unit_price) VALUES 
('VAC-V10', 'Vacina V10 Importada', 15, 85.00),
('VAC-RAB', 'Vacina Anti-Rábica', 0, 45.00),
('MED-VER', 'Vermífugo Drontal', 25, 30.00);